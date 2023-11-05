from typing import Any, Union, List

from pydantic import BaseModel
from sqlalchemy import Table, and_, func, select

from database import Database


class Query:
    _db: Database = None

    @classmethod
    def set_database(cls, db):
        cls._db = db

    @classmethod
    async def external_all(cls, stmt):
        return await cls._db.execute_all(stmt)

    @classmethod
    async def external_one(cls, stmt):
        return await cls._db.execute_one(stmt)

    def __init__(self, table: Table, parse_class):
        self.table = table
        self.parse_class = parse_class
        self.stmt = select(table)

    def _build_condition(self, kwargs: Any):
        conditions = []
        for key, value in kwargs.items():
            if key.endswith("__gte"):  # greater or equal
                key = key.replace("__gte", "")
                cond = self.table.columns[key] >= value
            elif key.endswith("__gt"):
                key = key.replace("__gt", "")
                cond = self.table.columns[key] > value
            elif key.endswith("__lte"):
                key = key.replace("__lte", "")
                cond = self.table.columns[key] <= value
            elif key.endswith("__lt"):
                key = key.replace("__lt", "")
                cond = self.table.columns[key] < value
            elif key.endswith("__in"):  # 'biba4756' in ['biba4756', 'qwew123']
                key = key.replace("__in", "")
                cond = self.table.columns[key].in_(value)
            elif key.endswith("__not_in"):
                key = key.replace("__not_in", "")
                cond = self.table.columns[key].notin_(value)
            elif key.endswith("__is_null"):
                key = key.replace("__is_null", "")
                if value:
                    cond = self.table.columns[key].is_(None)
                else:
                    cond = self.table.columns[key].isnot(None)
            else:
                cond = self.table.columns[key] == value
            conditions.append(cond)
        return and_(*conditions)

    def filter_by(self, **kwargs):
        conditions = self._build_condition(kwargs=kwargs)
        self.stmt = self.stmt.where(conditions)
        return self

    def like(self, column: str, value):
        self.stmt = self.stmt.where(self.table.columns[column].like(f'%{value}%'))
        return self

    def order_by(self, column: str, desc: bool = False):
        if desc:
            self.stmt = self.stmt.order_by(self.table.columns[column].desc())
        else:
            self.stmt = self.stmt.order_by(self.table.columns[column].asc())
        return self

    def limit(self, limit: int):
        self.stmt = self.stmt.limit(limit)
        return self

    def offset(self, offset: int):
        self.stmt = self.stmt.offset(offset)
        return self

    def group_by(self, **kwargs):
        pass

    def distinct(self):
        self.stmt = self.stmt.distinct()
        return self

    async def count(self):
        count_stmt = select(func.count().label("count")).select_from(self.stmt)
        count_all = await self._db.execute_one(count_stmt)
        return count_all.count

    async def all(self):
        result = await self._db.execute_all(self.stmt)
        return [self.parse_class.parse_obj(r) for r in result]

    async def one(self):
        result = await self._db.execute_one(self.stmt)
        if result is None:
            return None
        return self.parse_class.parse_obj(result)

    async def create(self, value: Union[BaseModel, dict]):
        value = value if isinstance(value, dict) else value.dict()
        stmt = self.table.insert().values(**value).returning(self.table)
        result = await self._db.execute_one(stmt)
        return self.parse_class.parse_obj(result)

    async def create_all(self, values: List[BaseModel]) -> None:
        stmts = [self.table.insert().values(**v.dict()) for v in values]
        await self._db.execute_many(stmts)

    async def update(self, values, **kwargs):
        stmt = self.table.update().values(values).where(self._build_condition(kwargs)).returning(self.table)
        result = await self._db.execute_one(stmt)
        return self.parse_class.parse_obj(result)

    async def delete(self, **kwargs):
        stmt = self.table.delete().where(self._build_condition(kwargs))
        return await self._db.execute_one(stmt)

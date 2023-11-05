from pydantic import BaseModel
from sqlalchemy import Table

from query import Query


class BaseConfig(BaseModel):
    class Config:
        use_enum_values = True


class DeclareTable(BaseModel, Query):
    _table: Table = None

    id: int

    @classmethod
    def query(cls) -> Query:
        return Query(table=cls._table, parse_class=cls)

    async def update_self(self):
        return await self.update(self.dict(), id=self.id)

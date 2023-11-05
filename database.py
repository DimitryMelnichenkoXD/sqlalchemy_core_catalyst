from sqlalchemy.ext.asyncio import create_async_engine


class Database:
    _instance = None
    _engine = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def init(cls, db_user: str, db_pass: str, db_host: str, db_name: str, db_type: str = "postgresql",
             db_engine: str = "asyncpg"):
        """
        Метод для инициализации ключевых данных для подключения базы данных
        """
        url = f"{db_type}+{db_engine}://{db_user}:{db_pass}@{db_host}/{db_name}"
        cls._engine = create_async_engine(url, echo=False)

    @classmethod
    async def execute_one(cls, statement):
        async with cls._engine.connect() as conn:
            result = await conn.execute(statement)
            result = result.fetchone()
            await conn.commit()
            return result

    @classmethod
    async def execute_all(cls, statement):
        async with cls._engine.connect() as conn:
            result = await conn.execute(statement)
            result = result.fetchall()
            await conn.commit()
            return result

    @classmethod
    async def execute_many(cls, statements: list):
        async with cls._engine.connect() as conn:
            for s in statements:
                await conn.execute(s)
            await conn.commit()

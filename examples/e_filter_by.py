import asyncio

from pydantic import BaseModel

from database import Database
from declare_table import DeclareTable
from query import Query


# Thus, the user object represents the table "user" in the database with defined columns and their properties.
# This object can be used to create, update and execute queries to this table in SQLAlchemy.

# metadata = sa.MetaData()
# user = sa.Table(
#     "user",
#     metadata,
#     sa.Column("id", sa.Integer, primary_key=True),
#     sa.Column("login", sa.String, nullable=False),
#     sa.Column("hash", sa.String, nullable=False),
#     sa.Column("salt", sa.String, nullable=False),
#     sa.Column("is_admin", sa.Boolean, default=False),
#     sa.Column("is_user", sa.Boolean, default=True)
# )


class UserABC(BaseModel):
    login: str
    hash: str
    salt: str
    is_admin: bool = False
    is_user: bool = True


class TableUser(UserABC, DeclareTable):
    # Is a variable that becomes a table object that represents a table in the database.
    # In this case, it is a table named "user".
    _table = None


async def run():
    db = Database()
    db.init(db_host="db_host", db_name="db_name", db_user="db_user", db_pass="db_pass")
    Query.set_database(db)
    user = await TableUser.query().filter_by(id=1).one()
    print(user)


asyncio.run(run())

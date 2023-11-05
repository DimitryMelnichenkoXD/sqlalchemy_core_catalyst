# import asyncio
#
# from pydantic import BaseModel
#
#
#
# class UserABC(BaseModel):
#     login: str
#     hash: str
#     salt: str
#     is_admin: bool
#     is_user: bool
#
#
# class TableUser(UserABC, DeclareTable):
#     _table = user
#
#
# async def run():
#     db_host = config.pg.host
#     db_name = config.pg.db
#     db_user = config.pg.username
#     db_pass = config.pg.password
#
#     db = Database()
#     db.init(db_host=db_host, db_name=db_name, db_user=db_user, db_pass=db_pass)
#     Query.set_database(db)
#     user = await TableUser.query().filter_by(id=1).one()
#     print(user)
#
#
# asyncio.run(run())

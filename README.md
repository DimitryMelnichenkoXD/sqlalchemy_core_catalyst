# SQLAlchemy-Core-Catalyst

SQLAlchemy-Core-Catalyst is a Python library that simplifies interactions with databases using SQLAlchemy and Pydantic. It provides a convenient way to define database models and perform CRUD (Create, Read, Update, Delete) operations with ease.

## Installation

You can install Your Library Name using `pip`:

```shell
pip install sqlalchemy-core-catalyst
```

## GitHub Repository

Explore the source code and contribute to the development of SQLAlchemyCoreCatalyst on GitHub.

- **GitHub Repository**: [GITHUB](https://github.com/DimitryMelnichenkoXD/sqlalchemy_core_catalyst/tree/main)

Feel free to fork the repository, open issues, and submit pull requests to help improve this project.

## Getting Started

Here is an example of how to use SQLAlchemy-Core-Catalyst to interact with a database:

```python
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
```
***
Try out and explore various examples in our playground [here](https://github.com/DimitryMelnichenkoXD/sqlalchemy_core_catalyst/tree/main/examples).
***

## Features

- **Database Interaction**: Simplify working with databases using SQLAlchemy. Define database tables with Pydantic models and perform queries with ease.

- **Easy Configuration**: Configure the library with simple parameters to connect to your database. No need for complex setup procedures.

- **Pydantic Integration**: Seamlessly integrate Pydantic models to define the structure of your data.

- **Simplified Queries**: Execute database queries with a straightforward and intuitive API, reducing the complexity of SQL.

- **Asynchronous Support**: Utilize asynchronous programming for efficient database interactions.

- **Highly Extensible**: Customize and extend the library to suit your specific project requirements.

- **Documentation**: Comprehensive documentation and examples to guide you through using the library effectively.

- **Open Source**: Licensed under the MIT License, allowing you to use and modify the library freely.

- **Community Support**: Active community and support for questions and issues.

These features make Your Library Name a powerful tool for managing database interactions, providing simplicity, flexibility, and efficiency.

## Documentation

For in-depth documentation, code examples, and additional resources, please visit the official documentation.

## License

This project is open-source and licensed under the MIT License. For complete details, see the LICENSE file included with the project.

## Acknowledgments

Please feel free to customize and expand this README according to the specific features, use cases, and documentation links associated with your library.
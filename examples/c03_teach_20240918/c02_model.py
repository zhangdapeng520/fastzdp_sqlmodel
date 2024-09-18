import sqlmodel
import typing


class Hero(sqlmodel.SQLModel, table=True):
    id: typing.Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    name: str
    real_name: str
    age: typing.Optional[int] = None

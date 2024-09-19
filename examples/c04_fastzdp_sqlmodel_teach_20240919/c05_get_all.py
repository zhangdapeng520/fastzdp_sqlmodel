from typing import Optional
from sqlmodel import Field, SQLModel
import fastzdp_sqlmodel as fasm


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


engine = fasm.get_engine(password="zhangdapeng520", database="fastzdp_sqlmodel", echo=True)
fasm.init_table(engine)

fasm.add(engine, User(name="张三"))
fasm.add(engine, User(name="李四"))

users = fasm.get_all(engine,User)
print(users)
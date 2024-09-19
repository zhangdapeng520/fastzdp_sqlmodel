from typing import Optional
from sqlmodel import Field, SQLModel
import fastzdp_sqlmodel as fasm


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int


engine = fasm.get_engine(password="zhangdapeng520", database="fastzdp_sqlmodel", echo=True)
fasm.init_table(engine)

fasm.add(engine, User(name="张三", age=22))
fasm.add(engine, User(name="李四", age=33))


data = {"name": "张三 333"}
fasm.update_id(engine, User,1, data)

u = fasm.get(engine, User, 1)
print("=======", u)

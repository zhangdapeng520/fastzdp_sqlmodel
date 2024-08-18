from typing import Optional
from sqlmodel import Field, SQLModel
import fastzdp_sqlmodel as fs


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: Optional[int] = None


# 创建数据库引擎
engine = fs.get_engine(database="fastzdp_sqlmodel")

# 初始化表格
fs.init_table(engine)

# 创建数据
fs.add(engine, User(name="张三1", age=23))
fs.add(engine, User(name="张三2", age=23))
fs.add(engine, User(name="张三3", age=23))

# 查询第一条数据
u = fs.get_first(engine, User, {"name": "张三1"})
print(u)

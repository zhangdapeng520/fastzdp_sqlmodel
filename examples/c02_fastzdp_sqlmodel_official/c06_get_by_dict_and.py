from typing import Optional
from sqlmodel import Field, SQLModel
import fastzdp_sqlmodel as fsqlmodel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: Optional[int] = None


# 创建数据库引擎
engine = fsqlmodel.get_engine(database="fastzdp_sqlmodel")

# 初始化表格
fsqlmodel.init_table(engine)

# 创建数据
u = User(name="张三", age=23)
fsqlmodel.add(engine, u)
u = User(name="张三", age=33)
fsqlmodel.add(engine, u)
u = User(name="李四", age=24)
fsqlmodel.add(engine, u)

# 查询年龄等于20或者小于30的用户
query = {"age": {">": 20, "<": 30}}
users = fsqlmodel.get_by_dict_and(engine, User, query)
print(users)

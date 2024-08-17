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

# 查询id为1的数据
u = fsqlmodel.get(engine, User, 1)
print(u)

# 删除
fsqlmodel.delete_id(engine, User, 1)

# 查询id为1的数据
u = fsqlmodel.get(engine, User, 1)
print(u)

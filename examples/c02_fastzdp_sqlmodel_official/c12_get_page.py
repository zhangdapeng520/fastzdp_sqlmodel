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
fsqlmodel.add(engine, User(name="张三1", age=23))
fsqlmodel.add(engine, User(name="张三2", age=23))
fsqlmodel.add(engine, User(name="张三3", age=23))

# 分页查询
result = fsqlmodel.get_page(engine, User, page=1, size=2)
print(result)

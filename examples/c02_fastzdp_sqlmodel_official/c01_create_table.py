from typing import Optional
from sqlmodel import Field, SQLModel
import fastzdp_sqlmodel as fsqlmodel


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


# 创建数据库引擎
engine = fsqlmodel.get_engine(database="fastzdp_sqlmodel")

# 删除所有表
SQLModel.metadata.drop_all(engine)

# 创建所有表
SQLModel.metadata.create_all(engine)

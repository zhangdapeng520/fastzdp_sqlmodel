from typing import Optional
from sqlmodel import Field, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


# 创建数据库引擎
sqlite_url = "mysql+pymysql://root:root@127.0.0.1:3306/fastzdp_sqlmodel?charset=utf8mb4"
engine = create_engine(sqlite_url, echo=True)

# 删除所有表
SQLModel.metadata.drop_all(engine)

# 创建所有表
SQLModel.metadata.create_all(engine)

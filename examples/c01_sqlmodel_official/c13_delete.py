from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session, select, or_


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)


# 创建数据库引擎
sqlite_url = "mysql+pymysql://root:root@127.0.0.1:3306/fastzdp_sqlmodel?charset=utf8mb4"
engine = create_engine(sqlite_url, echo=True)

# 创建所有表
SQLModel.metadata.drop_all(engine)
SQLModel.metadata.create_all(engine)

# 新增
u1 = User(name="张三1", age=23)
u2 = User(name="张三2", age=23)
u3 = User(name="张三3", age=23)

with Session(engine) as session:
    session.add(u1)
    session.add(u2)
    session.add(u3)
    session.commit()

# 查询
with Session(engine) as session:
    statement = select(User).where(User.name == "张三1")
    results = session.exec(statement)
    hero = results.one()
    print("User: ", hero)

    session.delete(hero)
    session.commit()
    print("Deleted hero:", hero)

    statement = select(User).where(User.name == "张三1")
    results = session.exec(statement)
    hero = results.first()
    if hero is None:
        print("不存在名字叫张三1的用户")

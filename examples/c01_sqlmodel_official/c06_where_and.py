from typing import Optional

from sqlmodel import Field, SQLModel, create_engine, Session, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


# 创建数据库引擎
sqlite_url = "mysql+pymysql://root:root@127.0.0.1:3306/fastzdp_sqlmodel?charset=utf8mb4"
engine = create_engine(sqlite_url, echo=True)

# 创建所有表
SQLModel.metadata.drop_all(engine)
SQLModel.metadata.create_all(engine)

# 新增
hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
hero_4 = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
hero_5 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
hero_6 = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
hero_7 = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)
with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.add(hero_4)
    session.add(hero_5)
    session.add(hero_6)
    session.add(hero_7)
    session.commit()

# and 查询
with Session(engine) as session:
    statement = select(Hero).where(Hero.age >= 35, Hero.age < 40)
    results = session.exec(statement)
    for hero in results:
        print(hero)

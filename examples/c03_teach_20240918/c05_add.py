from tkinter.font import names

import sqlmodel
import typing


class Hero(sqlmodel.SQLModel, table=True):
    id: typing.Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    name: str
    real_name: str
    age: typing.Optional[int] = None


db_url = "mysql+pymysql://root:zhangdapeng520@127.0.0.1:3306/fastzdp_sqlmodel?charset=utf8mb4"
engine = sqlmodel.create_engine(db_url, echo=True)

sqlmodel.SQLModel.metadata.drop_all(engine)
sqlmodel.SQLModel.metadata.create_all(engine)

# add
with sqlmodel.Session(engine) as session:
    zs1 = Hero(name="张三1", real_name="张三", age=33)
    session.add(zs1)
    zs2 = Hero(name="张三2", real_name="张三", age=33)
    session.add(zs2)
    zs3 = Hero(name="张三3", real_name="张三", age=33)
    session.add(zs3)

    session.commit()

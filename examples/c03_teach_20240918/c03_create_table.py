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
from typing import Optional
from sqlmodel import Field, SQLModel
import fastzdp_sqlmodel as fasm


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

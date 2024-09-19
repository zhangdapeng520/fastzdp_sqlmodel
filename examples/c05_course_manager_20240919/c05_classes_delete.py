from typing import Optional

from sqlmodel import Field, SQLModel
import fastzdp_sqlmodel as fasm


class Classes(SQLModel, table=True):
    """班级表"""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Course(SQLModel, table=True):
    """课程表"""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  # 课程名称
    class_id: Optional[int] = None  # 班级 ID
    class_name: Optional[str] = None  # 班级名称
    order: Optional[int] = 0  # 序号
    add_time: Optional[int] = None  # 添加时间
    price: int  # 价格


class CourseVideo(SQLModel, table=True):
    """课程视频表"""
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str  # 视频名称
    order: Optional[int] = 0  # 序号
    add_time: Optional[int] = None  # 添加时间
    course_id: Optional[int] = None  # 课程 ID
    course_name: Optional[str] = None  # 课程名称


engine = fasm.get_engine(password="zhangdapeng520", database="fastzdp_sqlmodel", echo=True)
fasm.init_table(engine)

fasm.add(engine, Classes(name="Python 零基础快速入门班"))
fasm.add(engine, Classes(name="FastAPI+Vue3 全栈班"))

fasm.delete_id(engine, Classes, 1)

data = fasm.get_all(engine, Classes)
print(data)
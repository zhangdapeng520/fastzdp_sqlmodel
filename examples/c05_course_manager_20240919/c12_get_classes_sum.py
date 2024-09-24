from typing import Optional
from sqlmodel import Field, SQLModel, Session, select, func
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

# 查询指定班级的所有课程的总价
query_dict = {"class_id": 14}
total = fasm.get_sum(engine, Course, "price", query_dict)
print(total)

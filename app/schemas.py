from pydantic import BaseModel
from datetime import date

class TeacherCreate(BaseModel):
    name: str
    email: str
    subject: str
    experience: int

class TeacherUpdate(BaseModel):
    name: str
    email: str
    subject: str
    experience: int

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str
    subject: str
    experience: int

    class Config:
        from_attributes = True  # Needed to work with SQLAlchemy ORM objects

# Lesson Plan Schemas
class LessonPlanCreate(BaseModel):
    teacher_id: int
    subject: str
    topic: str
    date: date
    details: str

class LessonPlanUpdate(BaseModel):
    teacher_id: int
    subject: str
    topic: str
    date: date
    details: str

class LessonPlanResponse(BaseModel):
    id: int
    teacher_id: int
    subject: str
    topic: str
    date: date
    details: str

    class Config:
        from_attributes = True

# Attendance Schemas
class AttendanceCreate(BaseModel):
    teacher_id: int
    student_id: int
    date: date
    present: bool

class AttendanceUpdate(BaseModel):
    teacher_id: int
    student_id: int
    date: date
    present: bool

class AttendanceResponse(BaseModel):
    id: int
    teacher_id: int
    student_id: int
    date: date
    present: bool

    class Config:
        from_attributes = True

# Grade Schemas
class GradeCreate(BaseModel):
    teacher_id: int
    student_id: int
    subject: str
    grade: str

class GradeUpdate(BaseModel):
    teacher_id: int
    student_id: int
    subject: str
    grade: str

class GradeResponse(BaseModel):
    id: int
    teacher_id: int
    student_id: int
    subject: str
    grade: str

    class Config:
        from_attributes = True


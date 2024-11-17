from pydantic import BaseModel
from typing import Optional

# Student schemas
class StudentBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    class_id: Optional[int] = None

class StudentCreate(StudentBase):
    pass

class StudentOut(StudentBase):
    id: int

    class Config:
        orm_mode = True

# Class schemas
class ClassBase(BaseModel):
    name: str

class ClassCreate(ClassBase):
    pass

class ClassOut(ClassBase):
    id: int

    class Config:
        orm_mode = True

# Subject schemas
class SubjectBase(BaseModel):
    name: str
    class_id: Optional[int] = None

class SubjectCreate(SubjectBase):
    pass

class SubjectOut(SubjectBase):
    id: int

    class Config:
        orm_mode = True

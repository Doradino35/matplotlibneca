from sqlalchemy.orm import Session
from app.models import Student, Class, Subject
from app.schemas import StudentCreate, ClassCreate, SubjectCreate

# CRUD operations for students
def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Student).offset(skip).limit(limit).all()

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def create_student(db: Session, student: StudentCreate):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# CRUD operations for classes
def get_class(db: Session, class_id: int):
    return db.query(Class).filter(Class.id == class_id).first()

def create_class(db: Session, class_data: ClassCreate):
    db_class = Class(**class_data.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

# CRUD operations for subjects
def get_subject(db: Session, subject_id: int):
    return db.query(Subject).filter(Subject.id == subject_id).first()

def create_subject(db: Session, subject_data: SubjectCreate):
    db_subject = Subject(**subject_data.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

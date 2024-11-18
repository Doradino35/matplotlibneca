from sqlalchemy.orm import Session
from app import models
from app import schemas
from fastapi import HTTPException, status

# Create a new teacher
def create_teacher(db: Session, teacher: schemas.TeacherCreate) -> models.Teacher:
    db_teacher = models.Teacher(
        name=teacher.name,
        email=teacher.email,
        subject=teacher.subject,
        experience=teacher.experience
    )
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

# Retrieve a teacher by ID
def get_teacher(db: Session, teacher_id: int) -> models.Teacher:
    teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if not teacher:
        print(f"Teacher with ID {teacher_id} not found") 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    print(f"Teacher found: {teacher}")  
    return teacher


# Retrieve all teachers with pagination
def get_teachers(db: Session, skip: int = 0, limit: int = 10) -> list[models.Teacher]:
    return db.query(models.Teacher).offset(skip).limit(limit).all()

# Update teacher details
def update_teacher(db: Session, teacher_id: int, teacher_data: schemas.TeacherUpdate) -> models.Teacher:
    teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    
    teacher.name = teacher_data.name
    teacher.email = teacher_data.email
    teacher.subject = teacher_data.subject
    teacher.experience = teacher_data.experience
    db.commit()
    db.refresh(teacher)
    return teacher

# Delete a teacher by ID
def delete_teacher(db: Session, teacher_id: int) -> None:
    teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    
    db.delete(teacher)
    db.commit()

# CRUD for Lesson Plans
def create_lesson_plan(db: Session, lesson_plan: schemas.LessonPlanCreate) -> models.LessonPlan:
    db_lesson_plan = models.LessonPlan(
        teacher_id=lesson_plan.teacher_id,
        subject=lesson_plan.subject,
        topic=lesson_plan.topic,
        date=lesson_plan.date,
        details=lesson_plan.details
    )
    db.add(db_lesson_plan)
    db.commit()
    db.refresh(db_lesson_plan)
    return db_lesson_plan

# Retrieve all lesson plans for a specific teacher
def get_lesson_plans_by_teacher_id(db: Session, teacher_id: int) -> list[models.LessonPlan]:
    return db.query(models.LessonPlan).filter(models.LessonPlan.teacher_id == teacher_id).all()

# CRUD for Attendance
def create_attendance(db: Session, attendance: schemas.AttendanceCreate) -> models.Attendance:
    db_attendance = models.Attendance(
        teacher_id=attendance.teacher_id,
        student_id=attendance.student_id,
        date=attendance.date,
        present=attendance.present
    )
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

# Retrieve attendance records for a specific teacher
def get_attendance(db: Session, teacher_id: int) -> list[models.Attendance]:
    return db.query(models.Attendance).filter(models.Attendance.teacher_id == teacher_id).all()

# CRUD for Grades
def create_grade(db: Session, grade: schemas.GradeCreate) -> models.Grade:
    db_grade = models.Grade(
        teacher_id=grade.teacher_id,
        student_id=grade.student_id,
        subject=grade.subject,
        grade=grade.grade
    )
    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)
    return db_grade

# Retrieve grades for a specific teacher
def get_grades(db: Session, teacher_id: int) -> list[models.Grade]:
    return db.query(models.Grade).filter(models.Grade.teacher_id == teacher_id).all()

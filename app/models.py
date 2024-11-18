from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    subject = Column(String)
    experience = Column(Integer)
    
    lesson_plans = relationship("LessonPlan", back_populates="teacher")
    attendance_records = relationship("Attendance", back_populates="teacher")
    grades = relationship("Grade", back_populates="teacher")

class LessonPlan(Base):
    __tablename__ = "lesson_plans"
    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    subject = Column(String, index=True)
    topic = Column(String)
    date = Column(Date)
    details = Column(String)

    teacher = relationship("Teacher", back_populates="lesson_plans")

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    student_id = Column(Integer)
    date = Column(Date)
    present = Column(Boolean)

    teacher = relationship("Teacher", back_populates="attendance_records")

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    student_id = Column(Integer)
    subject = Column(String)
    grade = Column(String)

    teacher = relationship("Teacher", back_populates="grades")

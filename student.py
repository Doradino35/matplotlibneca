from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import get_students, get_student, create_student
from app.schemas import StudentCreate, StudentOut
from app.database import get_db
from app.auth import get_current_user
from typing import List

router = APIRouter()

@router.get("/students/", response_model=List[StudentOut])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return get_students(db=db, skip=skip, limit=limit)

@router.get("/students/{student_id}", response_model=StudentOut)
def read_student(student_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    db_student = get_student(db=db, student_id=student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.post("/students/", response_model=StudentOut)
def create_new_student(student: StudentCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return create_student(db=db, student=student)
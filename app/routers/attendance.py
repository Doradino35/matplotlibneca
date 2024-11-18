from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.AttendanceCreate)
async def mark_attendance(attendance: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    """
    Mark attendance for a student on a specific date.
    Returns the marked attendance details.
    """
    return crud.create_attendance(db, attendance)

@router.get("/student/{student_id}", response_model=list[schemas.AttendanceCreate])
async def get_attendance_by_student(student_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get the attendance records for a specific student.
    Supports pagination.
    """
    return crud.get_attendance_by_student(db, student_id, skip=skip, limit=limit)

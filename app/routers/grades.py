from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud
from ..database import get_db

router = APIRouter()

# Create a grade record
@router.post("/", response_model=schemas.GradeResponse)
async def create_grade(grade: schemas.GradeCreate, db: Session = Depends(get_db)):
    return crud.create_grade(db=db, grade=grade)

# Get all grades for a teacher
@router.get("/{teacher_id}", response_model=List[schemas.GradeResponse])
async def get_grades(teacher_id: int, db: Session = Depends(get_db)):
    return crud.get_grades(db, teacher_id=teacher_id)

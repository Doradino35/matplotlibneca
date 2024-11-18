from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud
from ..database import get_db

router = APIRouter()

# Create a new lesson plan
@router.post("/", response_model=schemas.LessonPlanResponse)
async def create_lesson_plan(lesson_plan: schemas.LessonPlanCreate, db: Session = Depends(get_db)):
    return crud.create_lesson_plan(db=db, lesson_plan=lesson_plan)

# Get all lesson plans for a teacher
@router.get("/{teacher_id}", response_model=List[schemas.LessonPlanResponse])
async def get_lesson_plans(teacher_id: int, db: Session = Depends(get_db)):
    return crud.get_lesson_plans(db, teacher_id=teacher_id)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud,schemas
from app.database import get_db

router = APIRouter()

@router.post("/teachers/", response_model=schemas.TeacherResponse)
async def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return crud.create_teacher(db=db, teacher=teacher)

@router.get("/teachers/{teacher_id}", response_model=schemas.TeacherResponse)
async def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = crud.get_teacher(db, teacher_id=teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@router.get("/teachers/", response_model=list[schemas.TeacherResponse])
async def get_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_teachers(db, skip=skip, limit=limit)
 
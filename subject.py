from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import get_subject, create_subject
from app.schemas import SubjectCreate, SubjectOut
from app.database import get_db
from app.auth import get_current_user

router = APIRouter()

@router.get("/subjects/{subject_id}", response_model=SubjectOut)
def read_subject(subject_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return get_subject(db, subject_id)

@router.post("/subjects/", response_model=SubjectOut)
def create_new_subject(subject_in: SubjectCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return create_subject(db, subject_in)

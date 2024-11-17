from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud import get_class, create_class
from schemas import ClassCreate, ClassOut
from database import get_db
from auth import get_current_user

router = APIRouter()

@router.get("/classes/{class_id}", response_model=ClassOut)
def read_class(class_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return get_class(db, class_id)

@router.post("/classes/", response_model=ClassOut)
def create_new_class(class_in: ClassCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return create_class(db, class_in)

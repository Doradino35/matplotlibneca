from fastapi import FastAPI
from app.routers import teachers, lesson_plans, attendance, grades
from app.database import engine, Base


# Create all tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(teachers.router, prefix="/teachers", tags=["Teachers"])
app.include_router(lesson_plans.router, prefix="/lesson_plans", tags=["Lesson Plans"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])
app.include_router(grades.router, prefix="/grades", tags=["Grades"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the School Management System!"}





<<<<<<< HEAD
=======


>>>>>>> 2ba696d (comit)

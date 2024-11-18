from fastapi import FastAPI
from app.student import router as student_router
from app.classes import router as class_router
from app.subject import router as subject_router
from fastapi.routing import APIRouter  # Import APIRouter

app = FastAPI()


# Include routers
app.include_router(student_router, prefix="/students", tags=["students"])
app.include_router(class_router, prefix="/classes", tags=["classes"])
app.include_router(subject_router, prefix="/subjects", tags=["subjects"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the SkoolAsync Management System "}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
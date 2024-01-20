from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from crud import create_student, get_students, create_course, create_enrollment
from schemas import StudentCreate, CourseCreate, EnrollmentCreate

app = FastAPI()

@app.post("/students/")
def create_student_route(student: StudentCreate, db: Session = Depends(SessionLocal)):
    return create_student(db=db, name=student.name)

@app.get("/students/")
def read_students(db: Session = Depends(SessionLocal)):
    return get_students(db=db)

@app.post("/courses/")
def create_course_route(course: CourseCreate, db: Session = Depends(SessionLocal)):
    return create_course(db=db, name=course.name)

@app.post("/enrollments/")
def create_enrollment_route(enrollment: EnrollmentCreate, db: Session = Depends(SessionLocal)):
    return create_enrollment(db=db, student_id=enrollment.student_id, course_id=enrollment.course_id)

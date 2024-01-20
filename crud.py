from sqlalchemy.orm import Session
from models import Student, Course, Enrollment

def create_student(db: Session, name: str):
    student = Student(name=name)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

def get_students(db: Session):
    return db.query(Student).all()

# Similar functions for Course and Enrollment

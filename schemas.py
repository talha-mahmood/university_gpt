from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str

class CourseCreate(BaseModel):
    name: str

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

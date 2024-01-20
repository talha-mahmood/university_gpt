from fastapi import FastAPI
from uvicorn import run

from database import init_db
from models import Student, Course, Enrollment

app = FastAPI()

def main():
    init_db()

    # Example operations
    # You can add your application logic here

if __name__ == "__main__":
    run(app, host="127.0.0.1", port=8000, reload=True)

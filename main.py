from database import init_db, SessionLocal
from models import Student, Course, Enrollment
from fastapi import FastAPI

app = FastAPI()

def main():
    init_db()

    # Example operations
    with SessionLocal() as db:
        # Your application logic here
        pass  # Placeholder for your code

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

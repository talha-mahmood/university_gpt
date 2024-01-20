from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Replace 'username', 'password', 'dbname' with your PostgreSQL credentials
DATABASE_URL = "postgresql://talhamahmood1261:PDZYAQwI75Ok@ep-noisy-meadow-972632.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Create the tables
    Base.metadata.create_all(bind=engine)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Always place database in project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir))
DB_PATH = os.path.join(PROJECT_ROOT, 'courseflow.db')

# Get DATABASE_URL from environment variable or use default SQLite database
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DB_PATH}")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=False) # echo=True to see SQL in terminal

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models
Base = declarative_base()

# Optional helper to get session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Optional function to create all tables
def create_tables():
    Base.metadata.create_all(bind=engine)
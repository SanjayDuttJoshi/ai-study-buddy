"""
Database configuration and session management
SQLite setup with cross-platform path handling using pathlib
"""

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get the project root directory (cross-platform)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Database file path (cross-platform - works on Windows, Linux, macOS)
DB_PATH = BASE_DIR / "ai_study_buddy.db"

# Database URL for SQLite
DATABASE_URL = f"sqlite:///{DB_PATH}"

print(f"📁 Database will be created at: {DB_PATH}")

# Create SQLAlchemy engine
# connect_args is needed for SQLite to work with FastAPI (multithreading)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False  # Set to True for debugging SQL queries
)

# Create SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()


def get_db():
    """
    Dependency function to get database session
    
    Usage in FastAPI:
        @app.get("/users")
        def get_users(db: Session = Depends(get_db)):
            ...
    
    This ensures:
    - Each request gets its own database session
    - Session is automatically closed after request
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """
    Initialize database - create all tables
    
    This function:
    1. Imports all models (so SQLAlchemy knows about them)
    2. Creates all tables that don't exist yet
    3. Does NOT drop existing tables (safe to run multiple times)
    
    Call this on application startup in main.py
    """
    # Import all models here so SQLAlchemy knows about them
    from .models import User, HealthCheck  # noqa
    # Import future models as needed:
    # from .models import Note, Summary, Quiz, QuizAttempt, ChatMessage
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized successfully!")


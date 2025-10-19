"""
User Model
Handles user authentication and profile data
"""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..database import Base


class User(Base):
    """
    User model for authentication
    
    Table: users
    
    Fields:
    - id: Primary key (auto-increment)
    - username: Unique username (3-50 characters)
    - email: Unique email address
    - hashed_password: Bcrypt hashed password (never store plain text!)
    - created_at: Timestamp when user was created
    - updated_at: Timestamp when user was last updated
    
    Usage:
        # Create new user
        new_user = User(
            username="john",
            email="john@example.com",
            hashed_password=hashed_password
        )
        db.add(new_user)
        db.commit()
        
        # Query user
        user = db.query(User).filter(User.username == "john").first()
    """
    
    __tablename__ = "users"
    
    # Primary key - auto-increment integer
    id = Column(Integer, primary_key=True, index=True)
    
    # Username - unique, indexed for fast lookups
    username = Column(String(50), unique=True, index=True, nullable=False)
    
    # Email - unique, indexed
    email = Column(String(100), unique=True, index=True, nullable=False)
    
    # Hashed password - NEVER store plain passwords!
    hashed_password = Column(String(255), nullable=False)
    
    # Timestamps - automatically managed
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        """String representation for debugging"""
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"


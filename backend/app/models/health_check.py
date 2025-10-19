"""
Health Check Model
Example model to demonstrate database, API, and frontend integration
"""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..database import Base


class HealthCheck(Base):
    """
    Health Check model - Example for team learning
    
    This demonstrates:
    - How to create a database table
    - How to define columns
    - How to use timestamps
    
    Table: health_checks
    """
    
    __tablename__ = "health_checks"
    
    # Primary key - auto-increment
    id = Column(Integer, primary_key=True, index=True)
    
    # User's name
    name = Column(String(100), nullable=False)
    
    # Timestamp - automatically set when record is created
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        """String representation for debugging"""
        return f"<HealthCheck(id={self.id}, name='{self.name}')>"


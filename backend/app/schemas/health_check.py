"""
Health Check Schemas
Pydantic models for request/response validation
"""

from pydantic import BaseModel, Field
from datetime import datetime


class HealthCheckCreate(BaseModel):
    """
    Schema for creating a health check entry
    Used when frontend sends data to backend
    """
    name: str = Field(..., min_length=1, max_length=100, description="User's name")
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe"
            }
        }


class HealthCheckResponse(BaseModel):
    """
    Schema for health check response
    Used when backend sends data to frontend
    """
    id: int
    name: str
    created_at: datetime
    
    class Config:
        from_attributes = True  # Allows conversion from SQLAlchemy model
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "John Doe",
                "created_at": "2025-10-19T16:30:00"
            }
        }


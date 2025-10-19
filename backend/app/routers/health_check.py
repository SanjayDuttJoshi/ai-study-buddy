"""
Health Check Router
Example API endpoints demonstrating CRUD operations
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import HealthCheck
from ..schemas import HealthCheckCreate, HealthCheckResponse


router = APIRouter(
    prefix="/health-check",
    tags=["Health Check"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=HealthCheckResponse, status_code=201)
def create_health_check(
    health_check: HealthCheckCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new health check entry
    
    This endpoint demonstrates:
    - Receiving data from frontend (HealthCheckCreate)
    - Creating a database record
    - Returning the created record (HealthCheckResponse)
    
    Example:
        POST /health-check/
        Body: {"name": "John Doe"}
        Response: {"id": 1, "name": "John Doe", "created_at": "2025-10-19T16:30:00"}
    """
    # Create new HealthCheck instance
    db_health_check = HealthCheck(name=health_check.name)
    
    # Add to database session
    db.add(db_health_check)
    
    # Commit the transaction
    db.commit()
    
    # Refresh to get the id and created_at from database
    db.refresh(db_health_check)
    
    return db_health_check


@router.get("/", response_model=List[HealthCheckResponse])
def get_all_health_checks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get all health check entries
    
    This endpoint demonstrates:
    - Querying database
    - Pagination (skip & limit)
    - Returning list of records
    
    Parameters:
    - skip: Number of records to skip (for pagination)
    - limit: Maximum number of records to return
    
    Example:
        GET /health-check/?skip=0&limit=10
        Response: [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
    """
    health_checks = db.query(HealthCheck).offset(skip).limit(limit).all()
    return health_checks


@router.get("/{health_check_id}", response_model=HealthCheckResponse)
def get_health_check(
    health_check_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific health check entry by ID
    
    This endpoint demonstrates:
    - Getting single record by ID
    - Error handling (404 if not found)
    
    Example:
        GET /health-check/1
        Response: {"id": 1, "name": "John Doe", "created_at": "2025-10-19T16:30:00"}
    """
    health_check = db.query(HealthCheck).filter(HealthCheck.id == health_check_id).first()
    
    if health_check is None:
        raise HTTPException(status_code=404, detail="Health check entry not found")
    
    return health_check


@router.delete("/{health_check_id}", status_code=204)
def delete_health_check(
    health_check_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a health check entry
    
    This endpoint demonstrates:
    - Deleting a record
    - Error handling
    - 204 No Content response
    
    Example:
        DELETE /health-check/1
        Response: 204 No Content
    """
    health_check = db.query(HealthCheck).filter(HealthCheck.id == health_check_id).first()
    
    if health_check is None:
        raise HTTPException(status_code=404, detail="Health check entry not found")
    
    db.delete(health_check)
    db.commit()
    
    return None


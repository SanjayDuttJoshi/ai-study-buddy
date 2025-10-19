"""
API Client
Functions to communicate with backend API
"""

import requests
from typing import Dict, List, Optional

# Backend API base URL
BASE_URL = "http://localhost:8000"


def create_health_check(name: str) -> Dict:
    """
    Create a new health check entry
    
    Args:
        name: User's name
        
    Returns:
        Dictionary with created health check data
        
    Example:
        result = create_health_check("John Doe")
        # Returns: {"id": 1, "name": "John Doe", "created_at": "..."}
    """
    try:
        response = requests.post(
            f"{BASE_URL}/health-check/",
            json={"name": name}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def get_all_health_checks() -> List[Dict]:
    """
    Get all health check entries
    
    Returns:
        List of health check entries
        
    Example:
        entries = get_all_health_checks()
        # Returns: [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
    """
    try:
        response = requests.get(f"{BASE_URL}/health-check/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return []


def delete_health_check(health_check_id: int) -> bool:
    """
    Delete a health check entry
    
    Args:
        health_check_id: ID of the entry to delete
        
    Returns:
        True if successful, False otherwise
    """
    try:
        response = requests.delete(f"{BASE_URL}/health-check/{health_check_id}")
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False


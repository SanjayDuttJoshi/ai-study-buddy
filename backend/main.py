"""
AI Study Buddy - Backend API
Phase 0: Basic FastAPI Setup
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db
from app.routers import health_check

# Create FastAPI app
app = FastAPI(
    title="AI Study Buddy API",
    description="Backend API for AI-powered study companion",
    version="0.1.0"
)

# CORS middleware - allows frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    """Initialize database on startup"""
    print("🚀 Starting AI Study Buddy API...")
    init_db()
    print("✅ Database initialized!")


# Include routers
app.include_router(health_check.router)


@app.get("/")
def root():
    """
    Root endpoint - Health check
    """
    return {
        "message": "Welcome to AI Study Buddy API!",
        "status": "running",
        "version": "0.1.0",
        "phase": "Phase 0 - Basic Setup"
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


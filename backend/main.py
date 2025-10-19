"""
AI Study Buddy - Backend API
Phase 0: Basic FastAPI Setup
"""

from fastapi import FastAPI

# Create FastAPI app
app = FastAPI(
    title="AI Study Buddy API",
    description="Backend API for AI-powered study companion",
    version="0.1.0"
)


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


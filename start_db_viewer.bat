@echo off
REM Start Browser-Based Database Viewer (Windows)
REM Access at: http://localhost:8080

echo ========================================
echo 🌐 Starting Database Viewer...
echo ========================================
echo.
echo Database: ai_study_buddy.db
echo URL: http://localhost:8080
echo.
echo Press Ctrl+C to stop
echo ========================================
echo.

REM Activate virtual environment and start sqlite_web (note: underscore, not hyphen!)
call venv\Scripts\activate
sqlite_web ai_study_buddy.db --host 0.0.0.0 --port 8080


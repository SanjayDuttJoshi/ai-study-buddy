#!/bin/bash
# Start Browser-Based Database Viewer
# Access at: http://localhost:8080

echo "🌐 Starting Database Viewer..."
echo "================================"
echo ""
echo "Database: ai_study_buddy.db"
echo "URL: http://localhost:8080"
echo ""
echo "Press Ctrl+C to stop"
echo "================================"
echo ""

# Activate virtual environment and start sqlite_web (note: underscore, not hyphen!)
source venv/bin/activate
sqlite_web ai_study_buddy.db --host 0.0.0.0 --port 8080


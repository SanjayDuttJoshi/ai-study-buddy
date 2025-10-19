# Setup Guide - AI Study Buddy

Complete setup instructions for developers working on this project.

---

## 📋 Table of Contents

1. [Fresh Start (Without Cloning)](#fresh-start-without-cloning)
2. [Clone Setup (From GitHub)](#clone-setup-from-github)
3. [Prerequisites](#prerequisites)
4. [Quick Setup](#quick-setup)
5. [Running the Application](#running-the-application)
6. [Troubleshooting](#troubleshooting)
7. [Project Structure](#project-structure)

---

## 🆕 Fresh Start (Without Cloning)

If you want to create the project structure from scratch:

### Create Project Structure

```bash
# Create project folder
mkdir ai-study-buddy
cd ai-study-buddy

# Create backend structure
mkdir -p backend/app/routers
touch backend/main.py
touch backend/app/__init__.py
touch backend/app/routers/__init__.py

# Create frontend structure
mkdir -p frontend/pages frontend/utils
touch frontend/app.py
touch frontend/pages/__init__.py
touch frontend/utils/__init__.py

# Create requirements file
touch requirements.txt
```

### Add Dependencies to requirements.txt

```txt
# Phase 0 - Minimal Setup
fastapi==0.109.0
uvicorn[standard]==0.27.0
streamlit==1.30.0
python-dotenv==1.0.0
```

### Create Basic Backend (backend/main.py)

```python
from fastapi import FastAPI

app = FastAPI(
    title="AI Study Buddy API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to AI Study Buddy API!", "status": "running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Create Basic Frontend (frontend/app.py)

```python
import streamlit as st

st.set_page_config(page_title="AI Study Buddy", page_icon="📚")
st.title("🎓 AI Study Buddy")
st.success("✅ Frontend is running successfully!")
```

Now continue with [Quick Setup](#quick-setup) to install dependencies!

---


















## 📦 Clone Setup (From GitHub)

If you're cloning an existing repository:

### Step 1: Clone Repository

```bash
# Using HTTPS
git clone https://github.com/yourusername/ai-study-buddy.git
cd ai-study-buddy

# OR using SSH
git clone git@github.com:yourusername/ai-study-buddy.git
cd ai-study-buddy
```

### Step 2: Verify Structure

```bash
# Check if files exist
ls -la
# Should see: backend/, frontend/, requirements.txt, README.md
```

Now continue with [Quick Setup](#quick-setup)!

---

## 📋 Prerequisites

### Required Software

| Software | Version | Check Command |
|----------|---------|---------------|
| **Python** | 3.8 or higher | `python --version` or `python3 --version` |
| **pip** | Latest | `pip --version` or `pip3 --version` |
| **Git** | Latest (optional) | `git --version` |

### Installation Links

- **Python**: https://www.python.org/downloads/
- **Git**: https://git-scm.com/downloads

### Verify Python Installation

**Windows:**
```cmd
python --version
```

**Ubuntu/Linux/macOS:**
```bash
python3 --version
```

✅ Should show: `Python 3.8.x` or higher

---

## 🚀 Quick Setup

Choose your operating system:

### A. Windows Setup

#### Step 1: Open Command Prompt or PowerShell

```cmd
# Navigate to project folder
cd C:\path\to\ai-study-buddy
```

#### Step 2: Create Virtual Environment

```cmd
python -m venv venv
```

#### Step 3: Activate Virtual Environment

**Command Prompt:**
```cmd
venv\Scripts\activate
```

**PowerShell:**
```powershell
venv\Scripts\Activate.ps1
```

> **Note:** If PowerShell gives permission error:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

#### Step 4: Install Dependencies

```cmd
pip install -r requirements.txt
```

✅ You should see `(venv)` at the start of your prompt!

---

### B. macOS Setup

#### Step 1: Open Terminal

```bash
# Navigate to project folder
cd /path/to/ai-study-buddy
```

#### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
```

#### Step 3: Activate Virtual Environment

```bash
source venv/bin/activate
```

#### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

✅ You should see `(venv)` at the start of your prompt!

---

### C. Ubuntu/Linux Setup

#### Step 1: Open Terminal

```bash
# Navigate to project folder
cd /path/to/ai-study-buddy
```

#### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
```

#### Step 3: Activate Virtual Environment

```bash
source venv/bin/activate
```

#### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

✅ You should see `(venv)` at the start of your prompt!

---

## ▶️ Running the Application

You need to run **TWO servers** - Backend and Frontend in separate terminals.

### A. Windows

#### Terminal 1 - Backend

```cmd
# Activate virtual environment
venv\Scripts\activate

# Run backend
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

✅ Backend running at: http://localhost:8000

#### Terminal 2 - Frontend

```cmd
# Activate virtual environment (in new terminal)
venv\Scripts\activate

# Run frontend
cd frontend
streamlit run app.py --server.port 8501
```

✅ Frontend running at: http://localhost:8501

---

### B. Ubuntu/Linux & macOS

#### Terminal 1 - Backend

```bash
# Activate virtual environment
source venv/bin/activate

# Run backend
cd backend
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

✅ Backend running at: http://localhost:8000

#### Terminal 2 - Frontend

```bash
# Activate virtual environment (in new terminal)
source venv/bin/activate

# Run frontend
cd frontend
streamlit run app.py --server.port 8501
```

✅ Frontend running at: http://localhost:8501

---

## 🔍 Access URLs

Once both servers are running:

| Service | URL | Description |
|---------|-----|-------------|
| **Frontend** | http://localhost:8501 | Main application UI |
| **Backend** | http://localhost:8000 | API server |
| **API Docs** | http://localhost:8000/docs | Interactive API documentation (Swagger) |

---

## 🛑 Stopping the Application

In each terminal window:
```
Press: Ctrl + C
```

To deactivate virtual environment:
```bash
deactivate
```

---

## 🔧 Troubleshooting

### Issue 1: `python: command not found` (Linux/macOS)

**Problem:** Python command not recognized

**Solution:**
```bash
# Use python3 instead
python3 --version
python3 -m venv venv
```

---

### Issue 2: Virtual Environment Won't Activate (Windows PowerShell)

**Problem:** Execution policy error

**Solution:**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activating again
venv\Scripts\Activate.ps1
```

---

### Issue 3: Port Already in Use

**Problem:** Error says port 8000 or 8501 is already in use

**Solution:**

**Windows:**
```cmd
# Find process using port
netstat -ano | findstr :8000
netstat -ano | findstr :8501

# Kill process (replace <PID> with actual number)
taskkill /PID <PID> /F
```

**Linux/macOS:**
```bash
# Find process using port
lsof -i :8000
lsof -i :8501

# Kill process (replace <PID> with actual number)
kill -9 <PID>
```

---

### Issue 4: Module Not Found Error

**Problem:** `ImportError` or `ModuleNotFoundError`

**Solution:**
```bash
# Make sure virtual environment is activated
# You should see (venv) in your prompt

# Reinstall dependencies
pip install -r requirements.txt

# If specific package missing
pip install <package-name>
```

---

### Issue 5: Database Not Created

**Problem:** SQLite database file not appearing

**Solution:**
```bash
# Check if you're in the right directory
pwd  # Linux/macOS
cd   # Windows

# Database file should be at project root
ls ai_study_buddy.db  # Linux/macOS
dir ai_study_buddy.db # Windows

# If missing, restart backend - it will create automatically
```

---

### Issue 6: Backend Can't Connect to Frontend

**Problem:** CORS errors or connection refused

**Solution:**
1. Check backend is running: http://localhost:8000
2. Check CORS settings in `backend/main.py`
3. Verify `BACKEND_API_URL` in frontend code
4. Make sure no firewall blocking localhost

---

### Issue 7: Permission Denied (Linux/macOS)

**Problem:** Can't create files or run scripts

**Solution:**
```bash
# Give execute permission
chmod +x venv/bin/activate

# If creating files fails, check folder permissions
ls -la
```

---

### Issue 8: Streamlit Not Opening in Browser

**Problem:** Frontend runs but browser doesn't open

**Solution:**
1. Manually open: http://localhost:8501
2. Check if another app is using port 8501
3. Try different port:
   ```bash
   streamlit run app.py --server.port 8502
   ```

---

### Issue 9: Can't Install Packages

**Problem:** pip install fails

**Solution:**
```bash
# Upgrade pip first
python -m pip install --upgrade pip  # Windows
python3 -m pip install --upgrade pip # Linux/macOS

# Then try installing again
pip install -r requirements.txt
```

---

### Issue 10: Virtual Environment Not Working

**Problem:** Packages installing globally instead of in venv

**Solution:**
```bash
# Deactivate first
deactivate

# Delete old venv
rm -rf venv  # Linux/macOS
rmdir /s venv  # Windows

# Create fresh venv
python3 -m venv venv  # Linux/macOS
python -m venv venv   # Windows

# Activate and install
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
ai-study-buddy/
│
├── backend/                    # Backend API (FastAPI)
│   ├── app/                    # Application package
│   │   ├── __init__.py        # Package initializer
│   │   ├── database.py        # Database configuration (Phase 1+)
│   │   ├── models.py          # SQLAlchemy models (Phase 1+)
│   │   └── routers/           # Feature-based API routes
│   │       ├── __init__.py
│   │       └── auth.py        # Authentication endpoints (Phase 1)
│   └── main.py                # FastAPI app entry point
│
├── frontend/                   # Frontend UI (Streamlit)
│   ├── pages/                  # Feature-based pages
│   │   ├── __init__.py
│   │   ├── login.py           # Login page (Phase 1)
│   │   ├── register.py        # Registration page (Phase 1)
│   │   └── dashboard.py       # Main dashboard (Phase 1)
│   ├── utils/                  # Shared utilities
│   │   ├── __init__.py
│   │   ├── api_client.py      # Backend API communication
│   │   └── session.py         # Session management
│   └── app.py                  # Streamlit app entry point
│
├── venv/                       # Virtual environment (created by you)
│
├── ai_study_buddy.db          # SQLite database (created in Phase 1)
│
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview & features
├── SETUP.md                    # This file - Setup instructions
├── projectRequirementDevelopment.md  # Complete development plan
│
├── backend/PHASE1_TASKS.txt   # Backend Phase 1 tasks
└── frontend/PHASE1_TASKS.txt  # Frontend Phase 1 tasks
```

### File Purposes

| File/Folder | Purpose | Phase |
|-------------|---------|-------|
| `backend/main.py` | FastAPI app initialization | 0 |
| `backend/app/database.py` | Database connection setup | 1 |
| `backend/app/models.py` | Database table definitions | 1 |
| `backend/app/routers/auth.py` | Authentication API | 1 |
| `frontend/app.py` | Main app routing | 0 |
| `frontend/pages/login.py` | Login UI | 1 |
| `frontend/pages/register.py` | Registration UI | 1 |
| `frontend/pages/dashboard.py` | Dashboard UI | 1 |
| `frontend/utils/api_client.py` | API communication | 1 |
| `frontend/utils/session.py` | Session management | 1 |
| `requirements.txt` | Dependencies list | 0 |
| `ai_study_buddy.db` | SQLite database | 1 (auto-created) |

### Design Principles

**Backend:**
- ✅ Feature-based routing (each feature = one router file)
- ✅ Modular design (easy to add new features)
- ✅ Shared database connection
- ✅ All auth logic in `routers/auth.py`

**Frontend:**
- ✅ Page-based structure (each page = one file)
- ✅ `app.py` for routing only
- ✅ Shared utilities (API client, session)
- ✅ Each page is self-contained

**Benefits:**
- 🚀 Easy to find code (know where to look)
- 🚀 Easy to scale (add features without conflicts)
- 🚀 Team-friendly (multiple people work simultaneously)
- 🚀 Maintainable (change one feature = change one file)

---

## ✅ Verification Checklist

Before starting development:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] Virtual environment activated (see `(venv)` in prompt)
- [ ] Dependencies installed
- [ ] Backend starts without errors
- [ ] Frontend starts without errors
- [ ] Can access http://localhost:8000
- [ ] Can access http://localhost:8501
- [ ] No firewall blocking localhost

---

## 🎯 Next Steps

After successful setup:

1. ✅ **Phase 0 Complete** - Basic setup working
2. 📖 Read `backend/PHASE1_TASKS.txt` (Backend team)
3. 📖 Read `frontend/PHASE1_TASKS.txt` (Frontend team)
4. 👥 Divide tasks between team members
5. 🚀 Start implementing Phase 1 features
6. 🧪 Test integration between backend and frontend

---

## 📚 Additional Resources

- **FastAPI Tutorial**: https://fastapi.tiangolo.com/tutorial/
- **Streamlit Docs**: https://docs.streamlit.io/
- **SQLAlchemy Tutorial**: https://docs.sqlalchemy.org/en/14/tutorial/
- **Python Virtual Environments**: https://docs.python.org/3/tutorial/venv.html

---

## 🆘 Still Having Issues?

1. Check you're in the correct directory
2. Verify virtual environment is activated
3. Try restarting both servers
4. Check Python version is 3.8+
5. Review error messages carefully
6. Search error message online
7. Ask your team members

---

**Good luck with development! 🚀**

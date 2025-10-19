# 🏗️ Project Structure Guide

## Overview

This document explains the file organization and structure of the AI Study Buddy project. The project follows a **modular, feature-based architecture** where each component is organized by its functionality.

---

## 📁 Directory Structure

```
ai-study-buddy/
├── backend/                    # FastAPI backend application
│   ├── app/
│   │   ├── models/            # Database models (one file per entity)
│   │   │   ├── __init__.py    # Import all models here
│   │   │   └── user.py        # User model
│   │   ├── routers/           # API routes (one file per feature)
│   │   │   └── __init__.py
│   │   ├── database.py        # Database configuration
│   │   └── __init__.py
│   └── main.py                # FastAPI app entry point
│
├── frontend/                   # Streamlit frontend application
│   ├── pages/                 # Feature pages (to be created)
│   ├── utils/                 # Utility functions (to be created)
│   └── app.py                 # Streamlit app entry point
│
├── docs/                       # All documentation
│   ├── SETUP.md               # Setup instructions
│   ├── DATABASE_SETUP.md      # Database guide
│   ├── DATABASE_VIEWER.md     # DB viewer guide
│   ├── BACKEND_PHASE1_TASKS.txt  # Backend Phase 1 tasks
│   ├── PROJECT_STRUCTURE.md   # This file
│   └── projectRequirementDevelopment.md  # Full project plan
│
├── venv/                       # Virtual environment (not in Git)
├── ai_study_buddy.db          # SQLite database file (not in Git)
├── requirements.txt            # Python dependencies
├── start_db_viewer.sh         # Database viewer script (Linux/macOS)
├── start_db_viewer.bat        # Database viewer script (Windows)
├── view_database.py           # Python script to view database
└── README.md                   # Project overview
```

---

## 🎯 Design Principles

### 1. **Modular Architecture**
Each feature is isolated in its own file/folder:
- ✅ Easy to find code
- ✅ Multiple people can work simultaneously
- ✅ No merge conflicts
- ✅ Clean and organized

### 2. **Feature-Based Organization**
Code is organized by **what it does**, not by **what it is**:

**❌ Bad (Type-based):**
```
models.py          # ALL models in one file
routes.py          # ALL routes in one file
```

**✅ Good (Feature-based):**
```
models/
  ├── user.py      # User-related model
  ├── quiz.py      # Quiz-related model
  └── note.py      # Note-related model

routers/
  ├── auth.py      # Authentication routes
  ├── quiz.py      # Quiz routes
  └── notes.py     # Notes routes
```

### 3. **Single Responsibility**
Each file has **one clear purpose**:
- `user.py` → Only User model
- `auth.py` → Only authentication routes
- `quiz.py` → Only quiz-related logic

---

## 📂 Backend Structure (`/backend`)

### `main.py` - Application Entry Point
**Purpose:** Initialize FastAPI app, include routers, startup events

```python
from fastapi import FastAPI
from app.routers import auth, notes  # Import routers
from app.database import init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()  # Initialize database

# Include routers
app.include_router(auth.router)
app.include_router(notes.router)
```

**What goes here:**
- ✅ FastAPI app initialization
- ✅ Router imports and inclusion
- ✅ Middleware setup
- ✅ Startup/shutdown events
- ❌ NO business logic
- ❌ NO route definitions

---

### `app/database.py` - Database Configuration
**Purpose:** Database connection, session management, initialization

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    """Get database session"""
    ...

def init_db():
    """Initialize database tables"""
    ...
```

**What goes here:**
- ✅ Database connection setup
- ✅ Session management
- ✅ `get_db()` dependency
- ✅ `init_db()` function
- ❌ NO models
- ❌ NO queries

---

### `app/models/` - Database Models

#### Structure:
```
models/
├── __init__.py        # Import all models
├── user.py           # User model
├── note.py           # Note model (Phase 2)
├── summary.py        # Summary model (Phase 2)
├── quiz.py           # Quiz model (Phase 3)
└── chat.py           # Chat model (Phase 3)
```

#### `__init__.py` - Model Registry
**Purpose:** Centralized import point for all models

```python
from .user import User
from .note import Note
# Import other models...

__all__ = ["User", "Note", ...]
```

**Rules:**
- ✅ Import all models here
- ✅ Add to `__all__` list
- ❌ NO model definitions here

#### Individual Model Files (e.g., `user.py`)
**Purpose:** Define one database table

```python
from sqlalchemy import Column, Integer, String
from ..database import Base

class User(Base):
    """User model"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    ...
```

**Rules:**
- ✅ One model per file
- ✅ Clear docstrings
- ✅ Relationships with other models
- ❌ NO business logic
- ❌ NO routes

**When to create a new model file:**
- New database table needed
- Clear entity (User, Quiz, Note, etc.)
- Independent data structure

---

### `app/routers/` - API Routes

#### Structure:
```
routers/
├── __init__.py        # Empty (just a package marker)
├── auth.py           # Authentication routes
├── notes.py          # Notes CRUD routes (Phase 2)
├── content.py        # Content processing routes (Phase 2)
├── quiz.py           # Quiz routes (Phase 3)
└── chat.py           # Chat routes (Phase 3)
```

#### Individual Router Files (e.g., `auth.py`)
**Purpose:** Define routes for one feature

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(username: str, db: Session = Depends(get_db)):
    # Registration logic
    ...

@router.post("/login")
def login(credentials, db: Session = Depends(get_db)):
    # Login logic
    ...
```

**Rules:**
- ✅ One feature per file
- ✅ Use `APIRouter` not `app`
- ✅ Clear prefix and tags
- ✅ Include all related endpoints
- ❌ NO model definitions

**When to create a new router file:**
- New feature/functionality
- Group of related endpoints
- Clear API domain (auth, notes, quiz, etc.)

---

## 📂 Frontend Structure (`/frontend`)

### `app.py` - Application Entry Point
**Purpose:** Initialize Streamlit app, handle routing

```python
import streamlit as st

# App configuration
st.set_page_config(...)

# Routing logic
if not logged_in:
    show_login_page()
else:
    show_main_app()
```

**What goes here:**
- ✅ Streamlit configuration
- ✅ Page routing
- ✅ Session state management
- ❌ NO UI components (move to pages/)
- ❌ NO API calls (move to utils/)

---

### `pages/` - Feature Pages (To Be Created)

#### Structure:
```
pages/
├── login.py          # Login page
├── register.py       # Registration page
├── dashboard.py      # Main dashboard
├── notes.py          # Notes page
├── summarizer.py     # Summarizer page
├── quiz.py           # Quiz page
└── chat.py           # Chat page
```

#### Individual Page Files (e.g., `login.py`)
**Purpose:** Define UI for one page/feature

```python
import streamlit as st
from utils.api_client import login_user

def render():
    """Render login page"""
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        response = login_user(username, password)
        if response.success:
            st.success("Logged in!")
        ...
```

**Rules:**
- ✅ One page per file
- ✅ UI components only
- ✅ Call utilities for logic
- ❌ NO API calls here (use utils/)
- ❌ NO business logic

---

### `utils/` - Utility Functions (To Be Created)

#### Structure:
```
utils/
├── __init__.py       # Empty
├── api_client.py     # API communication
├── session.py        # Session management
└── helpers.py        # Helper functions
```

#### `api_client.py` - API Communication
**Purpose:** Handle all backend API calls

```python
import requests

BASE_URL = "http://localhost:8000"

def login_user(username, password):
    """Call login API"""
    response = requests.post(f"{BASE_URL}/auth/login", ...)
    return response.json()

def get_notes():
    """Get all notes"""
    ...
```

**Rules:**
- ✅ All API calls here
- ✅ Error handling
- ✅ Return parsed responses
- ❌ NO UI components

---

## 📂 Documentation (`/docs`)

### Purpose
All documentation files in one place (except README.md)

### Files:
- **SETUP.md** - Installation and setup guide
- **DATABASE_SETUP.md** - Database configuration guide
- **DATABASE_VIEWER.md** - How to use database viewer
- **BACKEND_PHASE1_TASKS.txt** - Backend Phase 1 tasks
- **PROJECT_STRUCTURE.md** - This file
- **projectRequirementDevelopment.md** - Full project plan

### Rules:
- ✅ All `.md` and `.txt` docs here
- ✅ Except `README.md` (stays at root)
- ✅ Organized and easy to find
- ❌ NO code files

---

## 🎯 How to Add New Features

### Adding a New Database Model

1. **Create model file:**
   ```bash
   touch backend/app/models/quiz.py
   ```

2. **Define model:**
   ```python
   # backend/app/models/quiz.py
   from sqlalchemy import Column, Integer, String
   from ..database import Base
   
   class Quiz(Base):
       __tablename__ = "quizzes"
       id = Column(Integer, primary_key=True)
       ...
   ```

3. **Register in `__init__.py`:**
   ```python
   # backend/app/models/__init__.py
   from .user import User
   from .quiz import Quiz  # Add this
   
   __all__ = ["User", "Quiz"]  # Add this
   ```

4. **Import in `database.py`:**
   ```python
   # backend/app/database.py
   def init_db():
       from .models import User, Quiz  # Add Quiz
       ...
   ```

---

### Adding a New API Route

1. **Create router file:**
   ```bash
   touch backend/app/routers/quiz.py
   ```

2. **Define routes:**
   ```python
   # backend/app/routers/quiz.py
   from fastapi import APIRouter
   
   router = APIRouter(prefix="/quiz", tags=["Quiz"])
   
   @router.get("/")
   def get_quizzes():
       ...
   ```

3. **Include in `main.py`:**
   ```python
   # backend/main.py
   from app.routers import quiz
   
   app.include_router(quiz.router)
   ```

---

### Adding a New Frontend Page

1. **Create page file:**
   ```bash
   touch frontend/pages/quiz.py
   ```

2. **Define page:**
   ```python
   # frontend/pages/quiz.py
   import streamlit as st
   from utils.api_client import get_quizzes
   
   def render():
       st.title("Quizzes")
       quizzes = get_quizzes()
       ...
   ```

3. **Add routing in `app.py`:**
   ```python
   # frontend/app.py
   from pages import quiz
   
   if page == "Quiz":
       quiz.render()
   ```

---

## ✅ Benefits of This Structure

### For Development:
- ✅ **Easy to navigate** - Clear file organization
- ✅ **No conflicts** - Multiple developers work simultaneously
- ✅ **Scalable** - Add features without mess
- ✅ **Maintainable** - Easy to find and fix bugs

### For Team:
- ✅ **Clear ownership** - Each file has a clear purpose
- ✅ **Easy onboarding** - New members understand quickly
- ✅ **Parallel work** - No blocking each other
- ✅ **Clean code** - Follows best practices

### For Learning:
- ✅ **Industry standard** - Real-world project structure
- ✅ **Best practices** - Modular, clean architecture
- ✅ **Professional** - Portfolio-ready code

---

## 🚀 Quick Reference

### Need to add...

| What | Where | File Name |
|------|-------|-----------|
| Database table | `backend/app/models/` | `entity_name.py` |
| API endpoints | `backend/app/routers/` | `feature_name.py` |
| Frontend page | `frontend/pages/` | `page_name.py` |
| API utility | `frontend/utils/` | `api_client.py` |
| Documentation | `docs/` | `DOC_NAME.md` |

---

## 📝 Summary

**Remember:**
1. **One feature = One file**
2. **Organize by function, not type**
3. **Keep files focused and small**
4. **Document as you go**
5. **Follow the established patterns**

**This structure helps us build a professional, scalable application while learning industry best practices!** 🎯

---

**Questions?** Check other docs in the [`docs/`](.) folder or ask your team!


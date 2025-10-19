# Database Setup - Already Configured! ✅

**Good news!** The database infrastructure is already set up and ready to use. Your team can focus on implementing business logic (CRUD operations, endpoints) without worrying about SQLAlchemy configuration.

---

## 📁 What's Already Done

### ✅ Files Created

1. **`backend/app/database.py`**
   - SQLite connection configured
   - Cross-platform path handling (works on Windows, Linux, macOS)
   - Session management setup
   - `get_db()` dependency function
   - `init_db()` initialization function

2. **`backend/app/models.py`**
   - User model defined
   - Future models ready to uncomment (Note, Summary, Quiz, etc.)
   - Proper relationships and constraints

3. **`backend/main.py`**
   - Database initialization on startup
   - CORS middleware configured
   - Ready for router imports

### ✅ Database Created

- **File**: `ai_study_buddy.db` (at project root)
- **Type**: SQLite
- **Tables**: `users` (ready for Phase 1)
- **Auto-created**: When backend starts

---

## 🎯 What Your Team Needs to Do

### Phase 1 Tasks:

#### Person A (Database & Models):
You DON'T need to create database.py or models.py - they're done!

**Your tasks:**
1. Study `backend/app/database.py` to understand how it works
2. Study `backend/app/models.py` to see the User model
3. Create CRUD operations in `backend/app/routers/auth.py`:
   ```python
   # Password hashing
   def get_password_hash(password: str) -> str
   def verify_password(plain_password: str, hashed_password: str) -> bool
   
   # User operations
   def create_user(db: Session, username: str, email: str, password: str)
   def get_user_by_username(db: Session, username: str)
   def authenticate_user(db: Session, username: str, password: str)
   ```

#### Person B (Authentication & API):
You DON'T need to setup database connection!

**Your tasks:**
1. Create schemas in `backend/app/routers/auth.py`
2. Create JWT functions in `backend/app/routers/auth.py`
3. Create API endpoints using the `get_db()` dependency
4. Uncomment router import in `backend/main.py`

---

## 📚 How to Use the Database

### 1. Import Database Session

```python
from sqlalchemy.orm import Session
from app.database import get_db
```

### 2. Use in API Endpoints

```python
from fastapi import Depends

@router.post("/auth/register")
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # db is automatically provided by FastAPI
    # Session is automatically closed after request
    
    # Use the database
    new_user = User(...)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
```

### 3. Query the Database

```python
from app.models import User

# Get user by username
user = db.query(User).filter(User.username == "john").first()

# Get user by email
user = db.query(User).filter(User.email == "john@example.com").first()

# Create new user
new_user = User(
    username="john",
    email="john@example.com",
    hashed_password=hashed_pw
)
db.add(new_user)
db.commit()
db.refresh(new_user)

# Update user
user.email = "newemail@example.com"
db.commit()

# Delete user
db.delete(user)
db.commit()
```

---

## 🔍 Database Structure

### Users Table (Phase 1)

```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
```

**Fields:**
- `id`: Auto-increment primary key
- `username`: Unique, 3-50 characters
- `email`: Unique email address
- `hashed_password`: Bcrypt hashed (NEVER store plain text!)
- `created_at`: Automatically set on creation
- `updated_at`: Automatically updated on modification

---

## 🧪 Testing Database

### Check if database exists:
```bash
ls -lh ai_study_buddy.db
```

### View tables:
```python
python3 -c "import sqlite3; conn = sqlite3.connect('ai_study_buddy.db'); cursor = conn.cursor(); cursor.execute('SELECT name FROM sqlite_master WHERE type=\"table\"'); print(cursor.fetchall())"
```

### Manual database reset (if needed):
```bash
# Delete database
rm ai_study_buddy.db

# Restart backend - it will recreate
cd backend
python3 -m uvicorn main:app --reload
```

---

## 🚀 Cross-Platform Features

### Path Handling
```python
# Uses pathlib for cross-platform compatibility
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "ai_study_buddy.db"
```

**Works on:**
- ✅ Windows: `C:\Users\...\ai_study_buddy.db`
- ✅ Linux: `/home/.../ai_study_buddy.db`
- ✅ macOS: `/Users/.../ai_study_buddy.db`

### SQLite Configuration
```python
# Allows FastAPI to work with SQLite multithreading
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
```

---

## 💡 Important Notes

### DO:
✅ Use `get_db()` dependency in endpoints
✅ Always commit after database changes
✅ Use `db.refresh()` to get updated data
✅ Let FastAPI close the session automatically

### DON'T:
❌ Store plain passwords (use bcrypt)
❌ Manually close database sessions (FastAPI does it)
❌ Query database outside FastAPI dependencies
❌ Forget to commit changes

---

## 🔄 Future Tables (Phase 2+)

Ready to uncomment in `models.py`:

```python
# Phase 2
- Note (for personal notes)
- Summary (for AI summaries)

# Phase 3
- Quiz (for quizzes)
- QuizAttempt (for quiz submissions)
- ChatMessage (for AI chat)
```

Just uncomment and run backend - tables auto-create!

---

## 📖 SQLAlchemy Resources

- **Tutorial**: https://docs.sqlalchemy.org/en/14/tutorial/
- **ORM Basics**: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
- **Querying**: https://docs.sqlalchemy.org/en/14/orm/queryguide.html

---

## 🆘 Common Questions

### Q: Where is the database file?
**A:** At project root: `ai_study_buddy.db`

### Q: How do I view the database?
**A:** Use DB Browser for SQLite (GUI) or python commands

### Q: Do I need to create tables?
**A:** No! They auto-create when backend starts

### Q: What if I break the database?
**A:** Delete `ai_study_buddy.db` and restart backend

### Q: How do I add a new table?
**A:** Uncomment model in `models.py`, restart backend

### Q: Can I use PostgreSQL instead?
**A:** Yes, in Phase 5 (deployment), just change DATABASE_URL

---

## ✅ Verification

Database is working if:
- [ ] Backend starts without errors
- [ ] File `ai_study_buddy.db` exists at project root
- [ ] Logs show "✅ Database initialized successfully!"
- [ ] Can import `from app.database import get_db`
- [ ] Can import `from app.models import User`

---

## 🎯 Summary

**What you have:**
- ✅ Configured SQLite database
- ✅ User model ready
- ✅ Session management setup
- ✅ Cross-platform compatibility

**What you do:**
- ✅ Implement CRUD functions
- ✅ Create API endpoints
- ✅ Use `get_db()` dependency
- ✅ Focus on business logic

**Database setup is DONE! Just use it! 🚀**


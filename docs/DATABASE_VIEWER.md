# 🌐 Browser-Based Database Viewer

## Quick Start

### Ubuntu/Linux/macOS:
```bash
./start_db_viewer.sh
```

### Windows:
```cmd
start_db_viewer.bat
```

### Then open in browser:
```
http://localhost:8080
```

---

## What is sqlite-web?

**sqlite-web** is a lightweight, browser-based SQLite database viewer - like FastAPI's `/docs` but for your database!

**Features:**
- ✅ Browser-based (no desktop app needed!)
- ✅ View all tables
- ✅ Browse data
- ✅ Run SQL queries
- ✅ Edit records inline
- ✅ Export to CSV/JSON
- ✅ Beautiful UI
- ✅ Lightweight (just a Python package)

---

## Manual Start

If scripts don't work:

### Ubuntu/Linux/macOS:
```bash
source venv/bin/activate
sqlite_web ai_study_buddy.db --host 0.0.0.0 --port 8080
```

### Windows:
```cmd
venv\Scripts\activate
sqlite_web ai_study_buddy.db --host 0.0.0.0 --port 8080
```

**Note:** The command is `sqlite_web` (underscore) not `sqlite-web` (hyphen)!

---

## Usage

### 1. Start the viewer
Run one of the startup scripts above

### 2. Open browser
Navigate to: http://localhost:8080

### 3. Explore
- **Tables tab**: See all tables
- **Query tab**: Run custom SQL
- **Structure tab**: View table schemas
- **Data tab**: Browse and edit records

---

## Features You'll See

### View Tables
- Click on any table name
- See all columns and data
- Paginated results

### Run SQL Queries
```sql
-- View all users
SELECT * FROM users;

-- Count users
SELECT COUNT(*) FROM users;

-- Search users
SELECT * FROM users WHERE username LIKE '%john%';
```

### Edit Data
- Click on any cell
- Edit inline
- Save changes

### Export Data
- Export to CSV
- Export to JSON
- Export to SQL

---

## Comparison with Other Tools

| Feature | sqlite-web | pgAdmin | DB Browser |
|---------|------------|---------|------------|
| **Interface** | Browser | Desktop | Desktop |
| **Installation** | pip install | Heavy | Medium |
| **Weight** | Lightweight | Heavy | Medium |
| **System Load** | Low | High | Medium |
| **Cross-platform** | ✅ | ✅ | ✅ |
| **Like /docs** | ✅ | ❌ | ❌ |

---

## Common Tasks

### View all tables:
1. Open http://localhost:8080
2. See list on left sidebar
3. Click any table to view

### Run a query:
1. Click "Query" tab
2. Type SQL query
3. Click "Execute"
4. See results

### Check table structure:
1. Click on table name
2. Click "Structure" tab
3. See columns, types, constraints

### Export data:
1. View table
2. Click "Export" button
3. Choose format (CSV/JSON/SQL)
4. Download

---

## Screenshots (What You'll See)

### Main Interface:
```
┌─────────────────────────────────────────┐
│  🗄️ ai_study_buddy.db                   │
├──────────┬──────────────────────────────┤
│ Tables   │                              │
│  • users │   [Table Content View]       │
│  • notes │                              │
│  • ...   │   Columns | Data | Structure│
│          │                              │
│          │   [Browse & Edit Data]       │
└──────────┴──────────────────────────────┘
```

### Query Interface:
```
┌─────────────────────────────────────────┐
│  SQL Query Editor                        │
├──────────────────────────────────────────┤
│  SELECT * FROM users;                    │
│                                          │
│  [Execute Query]                         │
├──────────────────────────────────────────┤
│  Results:                                │
│  ┌────┬──────────┬───────────────┐      │
│  │ id │ username │ email         │      │
│  ├────┼──────────┼───────────────┤      │
│  │ 1  │ john     │ john@mail.com │      │
│  └────┴──────────┴───────────────┘      │
└──────────────────────────────────────────┘
```

---

## Tips

### Use with Backend
Run both together:

**Terminal 1 - Backend:**
```bash
cd backend
python3 -m uvicorn main:app --reload
```

**Terminal 2 - Database Viewer:**
```bash
./start_db_viewer.sh
```

**Access:**
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Database: http://localhost:8080

### Safety
- ⚠️ Can edit data directly
- ⚠️ Changes are immediate
- ✅ Always backup before editing

### Performance
- ✅ Fast for small databases (< 100MB)
- ✅ Handles large tables well
- ✅ Pagination for big results

---

## Stopping the Viewer

Press `Ctrl + C` in the terminal where it's running

---

## Troubleshooting

### Port already in use:
```bash
# Use different port
sqlite-web ai_study_buddy.db --port 8081
```

### Can't access from browser:
- Check terminal - any errors?
- Verify URL: http://localhost:8080
- Try: http://127.0.0.1:8080

### Database locked:
- Stop backend first
- Or just view (don't edit)

---

## Alternatives (if sqlite-web doesn't work)

### Option 1: Use Python script
```bash
python3 view_database.py
```

### Option 2: SQLite CLI
```bash
sqlite3 ai_study_buddy.db
> .tables
> SELECT * FROM users;
```

### Option 3: VSCode Extension
- Install "SQLite" extension
- Right-click database file
- Select "Open Database"

---

## Why sqlite-web is Perfect

✅ **Browser-based** - No desktop app
✅ **Lightweight** - Just 1 Python package
✅ **Similar to /docs** - Familiar interface
✅ **No system load** - Runs only when needed
✅ **Cross-platform** - Works everywhere
✅ **Easy to use** - Intuitive UI

---

## Summary

**To view your database:**

1. **Start viewer:**
   ```bash
   ./start_db_viewer.sh  # Linux/Mac
   start_db_viewer.bat   # Windows
   ```

2. **Open browser:**
   ```
   http://localhost:8080
   ```

3. **Explore your data!** 🎉

**It's that simple!**

---

**No heavy desktop apps, just open your browser! 🌐**


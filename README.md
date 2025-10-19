# AI Study Buddy 🎓

An AI-powered study companion that helps students learn more efficiently through intelligent content summarization, interactive Q&A, automated quizzes, and progress tracking.

---

## 🌟 Overview

**AI Study Buddy** is your personal learning assistant that combines the power of AI with smart study tools to enhance your learning experience. Whether you're a high school student, college attendee, or self-learner, this app helps you study smarter, not harder.

---

## ✨ Features

### 🔐 Phase 1: User Authentication (Current)
- Secure user registration and login
- JWT-based authentication
- Password encryption
- Session management

### 📝 Phase 2: Notes & Content Processing (Coming Soon)
- **Smart Notes Management**
  - Create, edit, and organize study notes
  - Search and filter notes
  - Categorize by subjects
  
- **AI-Powered Summarization**
  - Upload PDF, DOCX, or TXT files
  - Get instant AI-generated summaries
  - Save time reading lengthy materials
  - Extract key concepts automatically

### 🤖 Phase 3: Interactive AI Features (Coming Soon)
- **AI Chat Assistant**
  - Ask questions and get instant answers
  - Clear doubts in real-time
  - Context-aware responses
  - Study-focused conversations

- **Quiz Generation**
  - Auto-generate quizzes from your materials
  - Multiple-choice questions with explanations
  - Immediate feedback
  - Learn from mistakes

### 📊 Phase 4: Progress Tracking (Coming Soon)
- **Personal Dashboard**
  - Track your learning progress
  - View quiz performance
  - Monitor study activity
  - Visual charts and graphs

- **Automated Scheduling**
  - Schedule recurring quizzes
  - Smart reminders
  - Spaced repetition system

---

## 🚀 Technology Stack

### Backend
- **FastAPI** - Modern, fast web framework
- **SQLite** - Lightweight database
- **SQLAlchemy** - Database ORM
- **Google Gemini AI** - AI capabilities
- **JWT** - Secure authentication

### Frontend
- **Streamlit** - Interactive web UI
- **Plotly** - Data visualization
- **Requests** - API communication

---

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

---

## ⚡ Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/ai-study-buddy.git
cd ai-study-buddy
```

### 2. Setup Virtual Environment

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run Backend (Terminal 1)

**Windows:**
```cmd
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Linux/macOS:**
```bash
cd backend
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Run Frontend (Terminal 2)

**Windows:**
```cmd
cd frontend
streamlit run app.py --server.port 8501
```

**Linux/macOS:**
```bash
cd frontend
streamlit run app.py --server.port 8501
```

### 5. Access Application

- **Frontend**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

For detailed setup instructions, see [SETUP.md](SETUP.md)

---

## 📖 Documentation

- **[SETUP.md](SETUP.md)** - Detailed setup and installation guide
- **[projectRequirementDevelopment.md](projectRequirementDevelopment.md)** - Complete development roadmap
- **[backend/PHASE1_TASKS.txt](backend/PHASE1_TASKS.txt)** - Backend Phase 1 tasks
- **[frontend/PHASE1_TASKS.txt](frontend/PHASE1_TASKS.txt)** - Frontend Phase 1 tasks

---

## 🏗️ Project Structure

```
ai-study-buddy/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── routers/     # Feature-based API routes
│   │   ├── database.py  # Database configuration
│   │   └── models.py    # Database models
│   └── main.py          # App entry point
│
├── frontend/             # Streamlit frontend
│   ├── pages/           # Feature pages
│   ├── utils/           # Utilities
│   └── app.py           # App entry point
│
└── requirements.txt      # Dependencies
```

---

## 🎯 Development Phases

### ✅ Phase 0: Project Setup (Complete)
- Project structure established
- Virtual environment configured
- Basic backend and frontend running

### 🔄 Phase 1: Authentication (In Progress)
- User registration
- Login system
- JWT authentication
- Session management

### 📅 Phase 2: Content & Notes (Planned)
- Notes CRUD operations
- File upload and processing
- AI summarization
- Content management

### 📅 Phase 3: AI Features (Planned)
- AI chatbot for Q&A
- Quiz generation
- Interactive learning

### 📅 Phase 4: Progress & Automation (Planned)
- Dashboard analytics
- Auto-scheduled quizzes
- Performance tracking

### 📅 Phase 5: Deployment (Planned)
- Production setup
- Cloud deployment
- Final optimizations

---

## 👥 Team Structure

**Backend Team (2 developers)**
- Person A: Database & Models
- Person B: Authentication & API

**Frontend Team (2 developers)**
- Person A: API Integration & Session
- Person B: UI Components & Pages

---

## 🤝 Contributing

This is a learning project. Each team member should:

1. Read their respective task file
2. Implement assigned features
3. Test thoroughly
4. Coordinate with team members
5. Learn by doing!

---

## 📊 Current Status

| Phase | Status | Progress |
|-------|--------|----------|
| Phase 0: Setup | ✅ Complete | 100% |
| Phase 1: Authentication | 🔄 In Progress | 0% |
| Phase 2: Content & Notes | 📅 Planned | 0% |
| Phase 3: AI Features | 📅 Planned | 0% |
| Phase 4: Progress & Automation | 📅 Planned | 0% |
| Phase 5: Deployment | 📅 Planned | 0% |

---

## 🎓 Learning Outcomes

Working on this project, you'll learn:

### Technical Skills
- ✅ FastAPI & REST API development
- ✅ Streamlit for web UI
- ✅ Database design with SQLAlchemy
- ✅ JWT authentication
- ✅ AI integration (Google Gemini)
- ✅ Git & version control

### Software Engineering
- ✅ Modular architecture
- ✅ Feature-based organization
- ✅ Clean code principles
- ✅ Team collaboration
- ✅ Testing & debugging

### Professional Skills
- ✅ Task division
- ✅ Project planning
- ✅ Documentation
- ✅ Problem-solving
- ✅ Code reviews

---

## 🛠️ Built With

- [Python](https://www.python.org/) - Programming language
- [FastAPI](https://fastapi.tiangolo.com/) - Backend framework
- [Streamlit](https://streamlit.io/) - Frontend framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM
- [Google Gemini](https://ai.google.dev/) - AI capabilities
- [SQLite](https://www.sqlite.org/) - Database

---

## 📄 License

This project is for educational purposes.

---

## 🙏 Acknowledgments

- Google Gemini AI for powering AI features
- FastAPI and Streamlit communities
- All team members and contributors

---

## 📞 Support

For setup help, see [SETUP.md](SETUP.md)

For development tasks, see:
- Backend: [backend/PHASE1_TASKS.txt](backend/PHASE1_TASKS.txt)
- Frontend: [frontend/PHASE1_TASKS.txt](frontend/PHASE1_TASKS.txt)

---

## 🎯 Vision

To create an intelligent study companion that makes learning more efficient, engaging, and personalized for every student.

---

**Built with ❤️ by students, for students**

**Start your journey to smarter studying today! 🚀**

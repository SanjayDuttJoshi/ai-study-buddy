# Project Requirements & Development Plan
## AI-Powered Study Buddy 🎓

---

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Development Phases](#development-phases)
4. [Feature Requirements](#feature-requirements)
5. [Cross-Platform Requirements](#cross-platform-requirements)

---

## 🎯 Project Overview

### Description
An AI-powered study companion that helps students learn more efficiently through content summarization, interactive Q&A, automated quizzes, and progress tracking.

### Core Value Proposition
- **Save Time**: Quick summaries of long study materials
- **Clear Doubts**: Instant AI-powered answers to questions
- **Test Knowledge**: Auto-generated quizzes with feedback
- **Track Progress**: Visual dashboard of learning metrics

### Target Users
- Students (High School, College, University)
- Self-learners and online course takers
- Anyone who wants to study more efficiently

---

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Database**: SQLite (SQLAlchemy ORM)
- **Authentication**: JWT (python-jose, passlib)
- **AI**: Google Gemini API
- **File Processing**: PyPDF2, python-docx

### Frontend
- **Framework**: Streamlit
- **API Client**: Requests
- **Visualization**: Plotly
- **Data Handling**: Pandas

### Development
- **Language**: Python 3.8+
- **Virtual Environment**: venv
- **Environment Variables**: python-dotenv
- **Version Control**: Git

---

## 📅 Development Phases

### **Phase 0: Project Setup & Foundation** ✅
**Goal**: Get basic frontend and backend running

**Tasks**:
1. Create project structure
2. Install core dependencies (FastAPI, Streamlit)
3. Create basic FastAPI app with health check
4. Create basic Streamlit app with welcome page
5. Setup virtual environment
6. Create requirements.txt
7. Test that both servers run successfully

**Success Criteria**:
- Backend runs on http://localhost:8000
- Frontend runs on http://localhost:8501
- Both show "Hello World" or basic page

**Deliverables**:
- Working FastAPI server
- Working Streamlit app
- Setup documentation

---

### **Phase 1: Core Backend & User Authentication** 🔐
**Goal**: Implement secure user registration and login

**Tasks**:
1. Setup database configuration (SQLite + SQLAlchemy)
2. Create User model
3. Implement password hashing
4. Create registration endpoint
5. Create login endpoint (JWT token generation)
6. Create authentication middleware
7. Test authentication flow

**API Endpoints**:
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login and get token
- `GET /auth/me` - Get current user info

**Database Models**:
- **User**:
  - id (Primary Key)
  - username (Unique)
  - email (Unique)
  - hashed_password
  - created_at
  - updated_at

**Success Criteria**:
- Users can register with username, email, password
- Users can login and receive JWT token
- Token expires after specified time
- Passwords are securely hashed

---

### **Phase 2: Content Processing & Notes Management** 📝
**Goal**: Allow users to upload documents, get AI summaries, and manage notes

#### Part A: Notes Management

**Tasks**:
1. Create Note model
2. Implement CRUD endpoints for notes
3. Ensure notes are user-specific
4. Create frontend notes page

**API Endpoints**:
- `POST /notes/` - Create note
- `GET /notes/` - Get all user notes
- `GET /notes/{id}` - Get specific note
- `PUT /notes/{id}` - Update note
- `DELETE /notes/{id}` - Delete note

**Database Models**:
- **Note**:
  - id (Primary Key)
  - user_id (Foreign Key)
  - title
  - content (Text)
  - created_at
  - updated_at

**Frontend Features**:
- Create note form
- List all notes
- Search/filter notes
- Edit note
- Delete note (with confirmation)

#### Part B: Content Summarization

**Tasks**:
1. Setup Gemini AI integration
2. Create file upload handling (PDF, TXT, DOCX)
3. Implement text extraction from files
4. Create summarization endpoint
5. Store summaries in database
6. Create frontend upload interface

**API Endpoints**:
- `POST /summaries/upload` - Upload file and summarize
- `POST /summaries/text` - Summarize pasted text
- `GET /summaries/` - Get all summaries
- `GET /summaries/{id}` - Get specific summary

**Database Models**:
- **Summary**:
  - id (Primary Key)
  - user_id (Foreign Key)
  - title
  - original_filename
  - original_content (Text)
  - summary_content (Text)
  - created_at

**File Processing**:
- Support PDF files
- Support TXT files
- Support DOCX files
- Extract text content
- Handle file size limits

**Success Criteria**:
- Users can create, read, update, delete notes
- Users can upload PDF/TXT/DOCX files
- AI generates accurate summaries
- Users can view all their summaries
- Each user only sees their own data

---

### **Phase 3: Interactive AI Features** 🤖
**Goal**: Build AI chatbot and quiz generation

#### Part A: Doubt Clearance Chatbot

**Tasks**:
1. Create chat endpoint
2. Integrate Gemini for Q&A
3. Store chat history
4. Create chat interface in frontend
5. Display chat history

**API Endpoints**:
- `POST /chat` - Send message to AI
- `GET /chat/history` - Get chat history

**Database Models**:
- **ChatMessage**:
  - id (Primary Key)
  - user_id (Foreign Key)
  - message (Text)
  - response (Text)
  - created_at

**Frontend Features**:
- Chat interface (message input + history)
- Real-time AI responses
- Chat history display
- Clear chat option

#### Part B: Quiz Generation

**Tasks**:
1. Create quiz generation logic with Gemini
2. Parse AI response into structured questions
3. Create quiz model
4. Implement quiz endpoints
5. Create quiz-taking interface
6. Implement grading system
7. Provide feedback with explanations

**API Endpoints**:
- `POST /quizzes/generate` - Generate quiz from content
- `GET /quizzes/` - Get all quizzes
- `GET /quizzes/{id}` - Get specific quiz
- `POST /quizzes/{id}/submit` - Submit answers and get score

**Database Models**:
- **Quiz**:
  - id (Primary Key)
  - user_id (Foreign Key)
  - title
  - topic
  - questions (JSON: [{question, options, correct_answer, explanation}])
  - created_at

- **QuizAttempt**:
  - id (Primary Key)
  - user_id (Foreign Key)
  - quiz_id (Foreign Key)
  - score (Float)
  - total_questions
  - answers (JSON: [selected_answers])
  - completed_at

**Quiz Format**:
- Multiple choice questions (4 options)
- Correct answer index
- Explanation for each question
- Configurable number of questions (1-20)

**Frontend Features**:
- Generate quiz from content
- Display questions one by one or all at once
- Submit answers
- Show score immediately
- Display correct answers with explanations
- Mark correct/incorrect answers

**Success Criteria**:
- Users can ask questions and get AI answers
- Chat history is saved
- Users can generate quizzes from any content
- Quiz questions are relevant and accurate
- Immediate grading with feedback
- Users can review their quiz attempts

---

### **Phase 4: Automation & Progress Tracking** 📈
**Goal**: Auto-schedule quizzes and provide progress dashboard

#### Part A: Progress Dashboard

**Tasks**:
1. Create aggregation queries for statistics
2. Calculate metrics (total notes, avg score, etc.)
3. Create dashboard endpoint
4. Build frontend dashboard with charts
5. Show recent activity
6. Display performance trends

**API Endpoints**:
- `GET /dashboard/stats` - Get user statistics

**Statistics to Display**:
- Total notes created
- Total summaries generated
- Total quizzes taken
- Average quiz score
- Recent activity (last 10 items)
- Quiz performance trend (chart)
- Study streak (optional)

**Frontend Features**:
- Key metrics cards
- Performance charts (Plotly)
- Recent activity feed
- Visual indicators (colors based on performance)
- Study tips section

#### Part B: Auto-Scheduled Quizzes

**Tasks**:
1. Install APScheduler
2. Create scheduler service
3. Add scheduling fields to Quiz model
4. Create schedule management endpoints
5. Implement background quiz creation
6. Add notification mechanism (optional)

**API Endpoints**:
- `POST /quizzes/{id}/schedule` - Schedule quiz repetition
- `GET /quizzes/scheduled` - Get scheduled quizzes
- `DELETE /quizzes/{id}/schedule` - Remove schedule

**Enhanced Quiz Model**:
- is_scheduled (Boolean)
- schedule_interval_days (Integer)
- next_scheduled_date (DateTime)

**Scheduler Features**:
- Schedule quiz to repeat every N days
- Auto-generate new quiz instance
- Send notification (email or in-app)
- View upcoming scheduled quizzes

**Success Criteria**:
- Dashboard shows accurate statistics
- Charts display performance trends
- Users can schedule quizzes
- Scheduled quizzes trigger automatically
- Users receive notifications

---

### **Phase 5: Frontend Integration & Polish** 🖥️
**Goal**: Complete UI/UX and prepare for deployment

**Tasks**:
1. Improve UI design and layout
2. Add error handling throughout
3. Implement loading states
4. Add confirmation dialogs
5. Create comprehensive documentation
6. Write deployment guide
7. Test on both Windows and Ubuntu
8. Performance optimization
9. Security review

**UI Improvements**:
- Consistent styling across pages
- Loading spinners for API calls
- Error messages in user-friendly format
- Success notifications
- Confirmation for destructive actions
- Responsive layout
- Dark mode (optional)

**Documentation**:
- Setup guide (detailed)
- User guide
- API documentation
- Troubleshooting guide
- Contribution guidelines

**Testing**:
- Test all features end-to-end
- Test on Windows OS
- Test on Ubuntu/Linux
- Test error scenarios
- Test file uploads (different formats)

**Success Criteria**:
- All features work smoothly
- No console errors
- Good user experience
- Works on both OS platforms
- Documentation is complete

---

## 🎨 Feature Requirements (Detailed)

### 1. User Authentication
- Minimum password length: 6 characters
- Username: 3-50 characters, unique
- Email: Valid email format, unique
- Token expiry: 30 minutes (configurable)
- Secure password hashing (bcrypt)

### 2. Notes Management
- Title: Maximum 200 characters
- Content: Text area, no limit
- Search: By title or content
- Sort: By creation date (newest first)
- Timestamps: Created and updated dates

### 3. Content Summarization
- Supported formats: PDF, TXT, DOCX
- Max file size: 10MB
- Summary length: Approximately 500 words
- Original content stored (first 5000 chars)
- Download summary as text file

### 4. AI Chatbot
- Real-time responses
- Conversation history stored
- Context-aware answers
- Study-focused prompts
- Clear chat option

### 5. Quiz Generation
- Questions per quiz: 1-20 (user choice)
- Question format: Multiple choice (4 options)
- Immediate feedback
- Score calculation: Percentage
- Explanation for each answer
- Review incorrect answers

### 6. Progress Dashboard
- Visual metrics display
- Performance charts
- Activity timeline
- Color-coded indicators
- Exportable reports (optional)

---

## 🌐 Cross-Platform Requirements

### Must Work On:
- **Windows 10/11**
- **Ubuntu 18.04+**
- **macOS 10.14+** (nice to have)

### Platform-Specific Considerations:

#### File Paths
- Use `pathlib.Path` for all file operations
- Never hardcode `/` or `\`
- Use `os.path.join()` where needed

#### Virtual Environment
- Document for both OS:
  - Windows: `python -m venv venv` & `venv\Scripts\activate`
  - Linux: `python3 -m venv venv` & `source venv/bin/activate`

#### Scripts
- Provide `.bat` files for Windows
- Provide `.sh` files for Linux/macOS
- Make scripts executable on Linux

#### Python Command
- Use `python3` for Linux/macOS
- Use `python` for Windows
- Document both in setup guide

---

## 📦 Dependencies by Phase

### Phase 0 (Setup)
```
fastapi==0.109.0
uvicorn[standard]==0.27.0
streamlit==1.30.0
python-dotenv==1.0.0
```

### Phase 1 (Authentication)
```
sqlalchemy==2.0.25
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
bcrypt==4.1.2
pydantic==2.5.3
```

### Phase 2 (Content & Notes)
```
google-generativeai==0.3.2
PyPDF2==3.0.1
python-docx==1.1.0
python-multipart==0.0.6
```

### Phase 3 (AI Features)
```
# Already included in Phase 2
```

### Phase 4 (Dashboard & Scheduling)
```
plotly==5.18.0
pandas==2.2.0
APScheduler==3.10.4
```

---

## 🔒 Security Requirements

1. **Password Security**
   - Hash all passwords before storage
   - Use bcrypt with sufficient rounds
   - Never log passwords

2. **Authentication**
   - JWT tokens with expiration
   - Secure secret key
   - Token refresh mechanism (optional)

3. **Data Access**
   - Users can only access their own data
   - Check user_id on all queries
   - Validate all inputs

4. **File Uploads**
   - Validate file types
   - Limit file sizes
   - Scan for malicious content (optional)
   - Use temporary storage

5. **API Security**
   - CORS configuration
   - Rate limiting (production)
   - Input validation
   - SQL injection protection (via ORM)

---

## 🎯 Success Metrics

### Technical Metrics
- API response time < 2 seconds (normal operations)
- AI response time < 10 seconds
- 100% of endpoints require authentication (except auth routes)
- Zero hardcoded credentials
- Works on Windows and Ubuntu

### User Experience Metrics
- User can complete signup in < 1 minute
- Summary generation in < 15 seconds
- Quiz generation in < 20 seconds
- Dashboard loads in < 3 seconds

---

## 📝 Development Workflow

### Step-by-Step Process:
1. Complete one phase fully before moving to next
2. Test after each feature implementation
3. Document as you build
4. Commit changes frequently
5. Test on both platforms regularly

### For Each Feature:
1. **Backend First**:
   - Create database models
   - Write API endpoints
   - Test with API docs (FastAPI Swagger)

2. **Frontend Second**:
   - Create UI components
   - Connect to API
   - Test user flow

3. **Integration**:
   - End-to-end testing
   - Error handling
   - User feedback (loading states, etc.)

---

## 🚀 Deployment Considerations (Future)

### Local Development
- Both backend and frontend run locally
- SQLite database in project folder
- Environment variables in `.env` file

### Production (Optional Future Phase)
- Deploy backend (Heroku, AWS, Railway)
- Deploy frontend (Streamlit Cloud)
- Use PostgreSQL instead of SQLite
- Implement proper logging
- Add monitoring
- Setup CI/CD pipeline

---

## 📞 Support & Maintenance

### Documentation Needed:
- Installation guide
- User manual
- API reference
- Troubleshooting guide
- FAQ section

### Future Enhancements:
- Study groups/collaboration
- Spaced repetition algorithm
- Mobile app
- Browser extension
- Integration with LMS platforms
- Multiple AI model support

---

**This document serves as the single source of truth for the entire project. Each phase should be completed and tested before moving to the next.**

**Current Status**: Phase 0 - Ready to begin setup 🚀


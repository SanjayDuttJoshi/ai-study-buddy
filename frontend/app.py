"""
AI Study Buddy - Frontend
Phase 0: Basic Streamlit Setup
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📚",
    layout="wide"
)

# Main page
st.title("🎓 AI Study Buddy")
st.markdown("### Your AI-Powered Learning Companion")

st.markdown("---")

# Welcome message
st.success("✅ Frontend is running successfully!")

st.info("""
**Phase 0: Setup Complete!**

This is the basic Streamlit frontend. Features will be added in upcoming phases:
- Phase 1: User Authentication
- Phase 2: Notes & Summaries
- Phase 3: AI Chat & Quizzes
- Phase 4: Progress Dashboard
""")

# Show some info
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🚀 Getting Started")
    st.markdown("""
    1. Backend should be running on port 8000
    2. Frontend is running on port 8501
    3. Ready for Phase 1 development!
    """)

with col2:
    st.markdown("#### 📋 Next Steps")
    st.markdown("""
    - Setup database (SQLite)
    - Implement user authentication
    - Add core features
    """)

# Footer
st.markdown("---")
st.caption("AI Study Buddy - Phase 0 | Backend: http://localhost:8000 | Frontend: http://localhost:8501")


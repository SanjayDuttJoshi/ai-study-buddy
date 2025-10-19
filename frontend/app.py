

import streamlit as st
from pages import health_check_page

# Page configuration
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
with st.sidebar:
    st.title("🎓 AI Study Buddy")
    st.markdown("---")
    
    page = st.radio(
        "Navigation",
        ["Home", "Health Check Example"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.caption("📚 Learning Project")

# Page routing
if page == "Home":
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
        3. Database viewer on port 8080
        4. Ready for Phase 1 development!
        """)
    
    with col2:
        st.markdown("#### 📋 Example Page")
        st.markdown("""
        👈 Check out the **Health Check Example** in the sidebar!
        
        It demonstrates:
        - How to create API endpoints
        - How to connect frontend to backend
        - How to save data to database
        - Complete CRUD operations
        """)
    
    # Footer
    st.markdown("---")
    st.caption("AI Study Buddy - Phase 0 | Backend: http://localhost:8000 | Frontend: http://localhost:8501")

elif page == "Health Check Example":
    health_check_page.render()


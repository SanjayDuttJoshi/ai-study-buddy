"""
Health Check Page
Example page demonstrating frontend-backend integration
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path to import utils
sys.path.append(str(Path(__file__).parent.parent))

from utils.api_client import create_health_check, get_all_health_checks, delete_health_check


def render():
    """
    Render the health check page
    
    This demonstrates:
    - Form input
    - API calls to backend
    - Displaying data from database
    - Delete functionality
    """
    
    st.title("🏥 Health Check - Example Page")
    st.markdown("### Learn how Frontend ↔️ Backend ↔️ Database works!")
    
    st.markdown("---")
    
    # Section 1: Create new entry
    st.subheader("1️⃣ Create Health Check Entry")
    st.info("**What happens:** Frontend → Backend API → Database")
    
    with st.form("health_check_form"):
        name = st.text_input(
            "Enter your name:",
            placeholder="John Doe",
            help="This will be saved to the database"
        )
        
        submit_button = st.form_submit_button("Submit", type="primary")
        
        if submit_button:
            if name.strip():
                with st.spinner("Saving to database..."):
                    result = create_health_check(name.strip())
                    
                if "error" in result:
                    st.error(f"❌ Error: {result['error']}")
                    st.warning("Make sure backend is running on http://localhost:8000")
                else:
                    st.success(f"✅ Successfully saved! ID: {result['id']}")
                    st.balloons()
                    # Rerun to refresh the list
                    st.rerun()
            else:
                st.warning("Please enter a name!")
    
    st.markdown("---")
    
    # Section 2: View all entries
    st.subheader("2️⃣ View All Entries")
    st.info("**What happens:** Frontend → Backend API → Database → Frontend")
    
    if st.button("🔄 Refresh List"):
        st.rerun()
    
    with st.spinner("Loading from database..."):
        entries = get_all_health_checks()
    
    if entries:
        st.success(f"Found {len(entries)} entries in database")
        
        # Display as table
        for entry in entries:
            col1, col2, col3, col4 = st.columns([1, 3, 3, 2])
            
            with col1:
                st.write(f"**ID:** {entry['id']}")
            
            with col2:
                st.write(f"**Name:** {entry['name']}")
            
            with col3:
                # Format datetime
                created = entry['created_at'].split('T')[0]
                st.write(f"**Created:** {created}")
            
            with col4:
                if st.button(f"🗑️ Delete", key=f"delete_{entry['id']}"):
                    if delete_health_check(entry['id']):
                        st.success(f"Deleted entry {entry['id']}")
                        st.rerun()
                    else:
                        st.error("Failed to delete")
            
            st.markdown("---")
    else:
        st.warning("No entries found. Create one above!")
    
    st.markdown("---")
    
    # Section 3: How it works
    with st.expander("📚 How This Works - For Learning"):
        st.markdown("""
        ### 🔄 Data Flow
        
        **When you submit the form:**
        1. **Frontend** (Streamlit) collects the name
        2. **Frontend** calls `create_health_check(name)` from `utils/api_client.py`
        3. **API Client** sends POST request to `http://localhost:8000/health-check/`
        4. **Backend** (`backend/app/routers/health_check.py`) receives request
        5. **Backend** creates `HealthCheck` model instance
        6. **Backend** saves to **Database** (SQLite)
        7. **Backend** returns created entry to **Frontend**
        8. **Frontend** shows success message
        
        ### 📁 Files Involved
        
        **Backend:**
        - `backend/app/models/health_check.py` - Database table definition
        - `backend/app/schemas/health_check.py` - Request/Response validation
        - `backend/app/routers/health_check.py` - API endpoints
        - `backend/main.py` - Includes the router
        - `backend/app/database.py` - Database connection
        
        **Frontend:**
        - `frontend/pages/health_check_page.py` - This page
        - `frontend/utils/api_client.py` - API communication
        
        **Database:**
        - `ai_study_buddy.db` - SQLite database file
        - Table: `health_checks` with columns: id, name, created_at
        
        ### 🎯 Key Concepts
        
        1. **Model** - Defines database table structure
        2. **Schema** - Validates request/response data
        3. **Router** - Handles API endpoints
        4. **API Client** - Frontend communicates with backend
        5. **CRUD** - Create, Read, Update, Delete operations
        
        ### 🔍 Check the Database
        
        Open the database viewer at: http://localhost:8080
        - Click on "health_checks" table
        - See the entries you created!
        """)
    
    # Footer
    st.markdown("---")
    st.caption("💡 **Tip:** Check backend logs and database viewer to see what's happening!")


if __name__ == "__main__":
    render()


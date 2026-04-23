import streamlit as st
import os

# 1. Path Logic: This ensures images load on Streamlit Cloud
# It looks for the 'assets' folder one level up from the 'pages' folder
base_path = os.path.dirname(__file__)

st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: #F5F2FF;
        }

        [data-testid="stSidebar"] {
            background: #EBE6FF;
        }
            
        .card {
            padding: 15px;
            border-radius: 15px;
            background-color: #ffffff;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            text-align: center;
            min-height: 250px;
        }

        .skill-label {
            font-weight: bold;
            color: #4B0082;
            margin-bottom: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🛠️ My Skills")

# --- Programming Languages Section ---
st.subheader("🚀 Programming Languages")
skills = {
    "Python": 50,
    "Java / XML / SQLite": 40,
    "Streamlit": 40,
    "HTML / CSS / JavaScript": 70
}

# Create a clean layout for progress bars
for skill, level in skills.items():
    st.markdown(f'<p class="skill-label">{skill}</p>', unsafe_allow_html=True)
    st.progress(level)

st.divider()

# --- Certificates Section ---
st.subheader("📜 Certificates")

# Data definition
skills_data = [
    {"name": "Python - Cisco Networking Academy", "img": "Python.png"},
    {"name": "Python - Simplilearn", "img": "python1.png"},
    {"name": "Java Programming", "img": "java.png"},
    {"name": "UI/UX Design", "img": "ui_ux.jpeg"},
    {"name": "Cybersecurity", "img": "cyber.jpg"},
    {"name": "Android Development", "img": "android.png"},
]

# Create the 3-column grid
for i in range(0, len(skills_data), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(skills_data):
            skill = skills_data[i + j]
            # Construct the path: go up one level from 'pages' to root, then into 'assets'
            img_path = os.path.join(base_path, "..", "assets", skill["img"])
            
            with cols[j]:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                
                # Check if file exists to prevent deployment crash
                if os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)
                else:
                    st.error("Image not found")
                
                st.caption(f"**{skill['name']}**")
                st.markdown('</div>', unsafe_allow_html=True)
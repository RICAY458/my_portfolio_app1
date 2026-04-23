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

# Make sure your filenames MATCH exactly what is in your GitHub assets folder
skills_data = [
    {"name": "Python - Cisco Networking Academy", "img": "Python.png"},
    {"name": "Python - Simplilearn", "img": "python1.png"},
    {"name": "Java Programming", "img": "java.png"},
    {"name": "UI/UX Design", "img": "ui_ux.jpeg"},
    {"name": "Cybersecurity", "img": "cyber.jpg"},
    {"name": "Android Development", "img": "android.png"},
]

# This logic prevents extra blank boxes
cols_per_row = 3
for i in range(0, len(skills_data), cols_per_row):
    cols = st.columns(cols_per_row)
    # Get the current chunk of 3 items
    chunk = skills_data[i : i + cols_per_row]
    
    for idx, skill in enumerate(chunk):
        with cols[idx]:
            # Construct the path
            img_path = os.path.join(base_path, "..", "assets", skill["img"])
            
            # We ONLY draw the card if the image exists
            if os.path.exists(img_path):
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.image(img_path, use_container_width=True)
                st.caption(f"**{skill['name']}**")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                # If image is missing, show a clear warning instead of a blank box
                st.warning(f"Missing: {skill['img']}")

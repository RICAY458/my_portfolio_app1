import streamlit as st
import os

# Get the directory that the current script is in, 
# then go up one level to find the 'assets' folder
base_path = os.path.dirname(__file__) # Points to the 'pages' folder
img_path = os.path.join(base_path, "..", "assets", "MYID2.png")


st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: #F5F2FF;
        }

        [data-testid="stSidebar"] {
            background: #EBE6FF;
        }
        
        .card {
            padding: 20px;
            border-radius: 15px;
            background-color: #ffffff;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)
# Header Section
st.title("✨ My Portfolio ✨")
st.subheader("Future Developer")

col1, col2 = st.columns([1,2])

with col1:
    st.image(img_path)

with col2:
    st.markdown("""
    ### Hi, I'm Rica Mae Sinogbujan👋!
    I am a passionate student developer creating modern applications.

    I build efficient, offline-capable systems and modern user interfaces.

    🚀 Explore my portfolio using the sidebar!
    """)
st.divider()

# Feature Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card">👤 <b> About Me</b><br>Explore to know more about me</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">🛠️ <b>Skills</b><br>My technical stack</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">💻 <b>Projects</b><br>Explore my work</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="card">📩 <b>Contact</b><br>Reach me easily</div>', unsafe_allow_html=True)
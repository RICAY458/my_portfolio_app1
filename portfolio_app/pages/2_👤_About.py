import streamlit as st


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

st.title("👤 About Me")

st.markdown("""
    <div class="card">
        I am a dedicated Computer Science student at DEBESMSCAT with hands-on experience in building applications and a passion for software development. 
        Despite being a student, I am willing to learn new technologies, and a commitment to continuous learning to support the company’s goals.
    </div>
""", unsafe_allow_html=True)

st.subheader("🎓 Education")

# --- START OF 3-COLUMN LAYOUT ---
# We create 3 columns to hold your 3 education levels
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="card">
            <h4>Primary</h4>
            <p>Calumpang Elementary School</p>
            <p>Calumpang, Cawayan, Masbate</p>
            <p>2006-2013</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card">
            <h4>Secondary</h4>
            <p>Dalipe National High School</p>
            <p>Dalipe, Cawayan, Masbate</p>
            <p>2013-2019</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="card">
            <h4>Tertiary</h4> 
            <p>BS Computer Science</p>
            <p>DEBESMSCAT</p> 
            <p>2023 - Present</p> 
        </div>
    """, unsafe_allow_html=True)
# --- END OF 3-COLUMN LAYOUT ---


st.subheader("🚀 Goals")
st.info("- Anroid Developer ")
st.info("- Web Front-end Developer ")
st.info("For now I will continue to enhance my skills as a beginner to become a professional Developer.")
# Fun interaction
mood = st.selectbox("How do you feel about coding?", ["😃 Love it", "🙂 Like it", "😅 It's okay"])
st.write("Your answer:", mood)
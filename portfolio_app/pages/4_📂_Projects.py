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

st.title("📁 My Projects")

st.markdown("""
    <div class="card">
        <h3>Library Management System</h3>
        <p>A Streamlit-based tool to manage the books in library and track who is students borrowed the books.</p>
        <a href="https://library-management-system0.streamlit.app/" target="_blank" class="live-link">
            🚀 View Live Library Management System
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="card">
        <h3>Student Grade Calculator</h3>
        <p>A Streamlit-based tool for automating academic performance tracking.</p>
        <a href="https://studentgradescalculator.streamlit.app/" target="_blank" class="live-link">
            🚀 View Live Student Grade Calculator
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="card">
        <h3>Home Appliances Inventory Management System</h3>
        <p>A web digital system the business owner can track their stocks.</p>
    </div>
""", unsafe_allow_html=True)
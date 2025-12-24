import streamlit as st
from datetime import date

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Mohammed Habeebuddin | Backend Developer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.main {
    background-color: #0e1117;
    color: #ffffff;
}

h1, h2, h3, h4 {
    color: #00e0ff;
}

.section {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(145deg, #111827, #0b1220);
    box-shadow: 0px 10px 30px rgba(0,0,0,0.6);
    margin-bottom: 30px;
}

.skill-box {
    padding: 12px;
    border-radius: 12px;
    background: #020617;
    border: 1px solid #1e293b;
    text-align: center;
}

.footer {
    text-align: center;
    opacity: 0.7;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "About Me",
        "Skills",
        "Projects",
        "Certifications",
        "Education",
        "Contact"
    ]
)

st.sidebar.markdown("---")
st.sidebar.write("**Role:** Backend Developer")
st.sidebar.write("**Tech:** Django | MySQL | Python")
st.sidebar.write("**Interest:** Product-Based Companies")

# ---------------- HOME ----------------
if page == "Home":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Mohammed Habeebuddin")
    st.subheader("Backend Developer | Django & MySQL Specialist")

    st.write("""
    I am a **final-year B.Tech Computer Science student** passionate about building
    **scalable backend systems**, **secure applications**, and **problem-solving products**
    using **Python, Django, and MySQL**.

    I focus on **clean architecture**, **database optimization**, and
    **real-world problem solving**, aligned with **product-based company expectations**.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Projects Built", "6+")
    col2.metric("Certifications", "8+")
    col3.metric("DSA Coverage", "Up to Graphs")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- ABOUT ----------------
elif page == "About Me":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("About Me")

    st.write("""
    I am currently pursuing **B.Tech in Computer Science** from **SR University, Warangal**.
    My core strength lies in **backend development**, with hands-on experience in:

    • Designing Django applications  
    • Relational database modeling using MySQL  
    • Secure authentication & authorization  
    • REST-like internal logic (without external APIs)  
    • Writing clean, maintainable Python code  

    I strongly believe in **learning by building** and continuously improving through
    **DSA practice**, **real projects**, and **system thinking**.
    """)

    st.info("🎯 Career Goal: Become a strong backend engineer in a product-based company")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SKILLS ----------------
elif page == "Skills":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("Technical Skills")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Backend")
        st.progress(90)
        st.write("Python")
        st.progress(85)
        st.write("Django")
        st.progress(80)
        st.write("MySQL")

    with col2:
        st.subheader("Frontend")
        st.progress(75)
        st.write("HTML")
        st.progress(70)
        st.write("CSS / Bootstrap")
        st.progress(65)
        st.write("JavaScript")

    with col3:
        st.subheader("Core CS")
        st.progress(80)
        st.write("Data Structures & Algorithms")
        st.progress(70)
        st.write("DBMS")
        st.progress(65)
        st.write("OS & CN")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif page == "Projects":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("Major Projects")

    with st.expander("🔐 Password Manager (Python + MySQL)"):
        st.write("""
        • Secure password storage using encryption  
        • Password strength analyzer  
        • CLI + optional UI version  
        • MySQL database for persistence  
        • Focus on security & clean logic
        """)

    with st.expander("📅 Priority Planner (Django + MySQL)"):
        st.write("""
        • Task scheduling & priority management  
        • User authentication  
        • CRUD operations with Django ORM  
        • Deployed with production-ready settings  
        """)

    with st.expander("🏦 Banking Management System"):
        st.write("""
        • Account creation & transaction handling  
        • MySQL relational schema  
        • Python backend logic  
        • Emphasis on data consistency
        """)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- CERTIFICATIONS ----------------
elif page == "Certifications":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("Certifications")

    st.write("""
    ✔ AWS Cloud Web Application Builder  
    ✔ Azure Fundamentals  
    ✔ Artificial Intelligence Certification  
    ✔ Cybersecurity & Ethical Hacking  
    ✔ Python Programming  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- EDUCATION ----------------
elif page == "Education":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("Education")

    st.write("""
    **B.Tech – Computer Science Engineering**  
    SR University, Warangal  
    Final Year  

    Focus Areas:
    • Backend Engineering  
    • Database Systems  
    • Algorithms  
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- CONTACT ----------------
elif page == "Contact":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.header("Contact Me")

    st.write("📧 Email: habeebuddin@example.com")
    st.write("💼 LinkedIn: linkedin.com/in/habeebuddin")
    st.write("💻 GitHub: github.com/yourusername")

    st.success("Open to Backend / Django / Product-Based Opportunities")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("<div class='footer'>© 2025 Mohammed Habeebuddin | Backend Developer</div>", unsafe_allow_html=True)

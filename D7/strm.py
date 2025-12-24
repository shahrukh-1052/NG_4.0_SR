# app.py
import streamlit as st
from datetime import date
from io import BytesIO

# -------------------------------
# Page config and theme
# -------------------------------
st.set_page_config(
    page_title="MOHAMMED | Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------------
# Minimal CSS for polish
# -------------------------------
CSS = """
<style>
/* Global reset for clean look */
html, body, [class*="css"] {
    font-family: 'Inter', 'Segoe UI', Roboto, -apple-system, system-ui, sans-serif;
}

/* Headings and spacing */
h1, h2, h3 { margin-bottom: 0.25rem; }
section { margin-bottom: 1.25rem; }

/* Card style */
.card {
    border-radius: 12px;
    padding: 16px;
    border: 1px solid rgba(0,0,0,0.08);
    background: linear-gradient(180deg, rgba(255,255,255,0.75), rgba(255,255,255,0.6));
    backdrop-filter: blur(4px);
}

/* Tags */
.tag {
    display: inline-block;
    padding: 4px 10px;
    margin: 4px 8px 4px 0;
    border-radius: 999px;
    font-size: 12px;
    background: #eef3ff;
    color: #1f4fff;
    border: 1px solid #dbe3ff;
}

/* Subtle divider */
.divider {
    height: 1px;
    background: linear-gradient(to right, transparent, rgba(0,0,0,0.1), transparent);
    margin: 16px 0;
}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# -------------------------------
# Sidebar navigation
# -------------------------------
PAGES = {
    "About": "about",
    "Skills": "skills",
    "Projects": "projects",
    "Experience": "experience",
    "Education": "education",
    "Contact": "contact",
}

with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/9919?s=200&v=4", width=80)  # Replace with your photo URL or local path
    st.markdown("### MOHAMMED")
    st.write("Hasanparthy, TG, India")
    st.write("Python • Django • ML • REST APIs • Git")
    st.markdown("---")
    page = st.radio("Navigate", list(PAGES.keys()))
    st.markdown("---")
    # Socials
    st.markdown("#### Connect")
    st.write("[GitHub](https://github.com/yourusername)")
    st.write("[LinkedIn](https://www.linkedin.com/in/yourusername)")
    st.write("[Email](mailto:your@email.com)")
    st.write("[Portfolio site](https://yourdomain.com)")

# -------------------------------
# Helper components
# -------------------------------
def pill_tags(tags):
    html = "".join([f"<span class='tag'>{t}</span>" for t in tags])
    st.markdown(html, unsafe_allow_html=True)

def card(title, body="", tags=None, link=None):
    with st.container():
        st.markdown(f"<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"**{title}:** {body}")
        if tags:
            pill_tags(tags)
        if link:
            st.markdown(f"[Open]({link})")
        st.markdown(f"</div>", unsafe_allow_html=True)

def download_resume(resume_bytes: bytes, filename="MOHAMMED_Resume.pdf"):
    st.download_button(
        label="Download resume",
        data=resume_bytes,
        file_name=filename,
        mime="application/pdf",
    )

# -------------------------------
# Sample resume file (placeholder)
# -------------------------------
def build_placeholder_resume():
    # Replace with actual PDF bytes (read from file)
    placeholder_text = """
    MOHAMMED — Resume (Placeholder)
    Location: Hasanparthy, TG, India
    Skills: Python, Django, Django REST, ML, Git, Streamlit, Data Visualization
    Experience: Describe your roles and achievements with measurable outcomes.
    Projects: Summarize impact, performance, scalability, and user outcomes.
    Education: Your degree(s) and notable coursework/certifications.
    """
    # Create a simple bytes object to enable download; use a real PDF in production
    return BytesIO(placeholder_text.encode("utf-8")).getvalue()

# -------------------------------
# Page: About
# -------------------------------
def render_about():
    st.title("About")
    st.write(
        "I build clean, scalable, and data-driven products—combining Python, Django REST APIs, ML pipelines, and modern UI clarity. "
        "I care about robust workflows, privacy-conscious design, and solutions that feel simple but perform professionally."
    )
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.metric("Experience", "2–4 years", "Product + Research")
    with col2:
        st.metric("Focus", "Python/Django", "ML + REST APIs")
    with col3:
        st.metric("Location", "Hasanparthy, TG", "India")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("Highlights")
    st.markdown("- **Ownership:** End-to-end execution from architecture to delivery\n"
                "- **Clarity:** Readable code, intentional UI, documented APIs\n"
                "- **Impact:** Measurable outcomes, performance baselines, reproducible pipelines")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    resume_bytes = build_placeholder_resume()
    download_resume(resume_bytes)

# -------------------------------
# Page: Skills
# -------------------------------
def render_skills():
    st.title("Skills")
    st.subheader("Core")
    st.markdown(
        "- **Languages:** Python\n"
        "- **Frameworks:** Django, Django REST Framework, Streamlit\n"
        "- **ML/Data:** Pandas, NumPy, scikit-learn, PyTorch (basic), XGBoost\n"
        "- **DevOps/Tools:** Git/GitHub, GitLab CI, Docker (basic), VS Code\n"
        "- **Web/UI:** HTML basics, responsive design principles, accessible color/contrast"
    )
    st.subheader("Complementary")
    st.markdown(
        "- **APIs:** REST design, pagination, auth, rate limiting\n"
        "- **Testing:** PyTest, unit/integration tests\n"
        "- **Performance:** profiling, caching, query optimization\n"
        "- **Docs:** OpenAPI/Swagger, README and usage guides"
    )
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("Tech stack tags")
    pill_tags(["Python", "Django", "DRF", "Streamlit", "Pandas", "NumPy", "scikit-learn", "Git", "Docker", "PyTorch (basic)"])

# -------------------------------
# Page: Projects
# -------------------------------
def render_projects():
    st.title("Projects")

    st.subheader("Featured")
    col1, col2 = st.columns(2)
    with col1:
        card(
            "Smart Job-Match REST API",
            "A Django REST service that ranks candidates and roles using ML features and clean scoring. Includes authentication, pagination, filters, and CI.",
            tags=["Django", "DRF", "ML features", "GitHub Actions", "PostgreSQL"],
            link="https://github.com/yourusername/job-match-api",
        )
    with col2:
        card(
            "Readable Analytics Dashboard",
            "Streamlit app with intentional color and shadow choices for clarity. Live data, filters, and export-ready visuals for stakeholders.",
            tags=["Streamlit", "Pandas", "Altair", "Design clarity"],
            link="https://github.com/yourusername/readable-analytics",
        )

    col3, col4 = st.columns(2)
    with col3:
        card(
            "ML Pipeline Orchestrator",
            "Lightweight training/inference pipeline with versioned datasets, feature views, and experiment logs.",
            tags=["scikit-learn", "XGBoost", "ML Ops (basic)", "DVC (optional)"],
            link="https://github.com/yourusername/ml-pipeline-orchestrator",
        )
    with col4:
        card(
            "Clean Django Starter",
            "Production-ready starter with a sensible app layout, settings split, .env handling, and user auth.",
            tags=["Django", "Best practices", "Auth", "Settings"],
            link="https://github.com/yourusername/django-clean-starter",
        )

# -------------------------------
# Page: Experience
# -------------------------------
def render_experience():
    st.title("Experience")

    card(
        "Software Developer — Product-focused",
        "Delivered data apps and REST APIs with measurable speed and reliability improvements. Led clean Git workflows, code reviews, and documentation.",
        tags=["Python", "Django", "DRF", "Git", "CI/CD"],
    )
    card(
        "Research/Intern — ML + Data",
        "Implemented feature engineering and model baselines with reproducible notebooks and pipeline scripts.",
        tags=["Pandas", "scikit-learn", "XGBoost", "Evaluation"],
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("Outcome snapshots")
    st.markdown(
        "- **Latency:** Cut API p95 by **35%** via query optimization and caching\n"
        "- **Reliability:** Increased test coverage to **85%** and reduced rollbacks\n"
        "- **Adoption:** Drove stakeholder usage with clearer dashboards and docs"
    )

# -------------------------------
# Page: Education
# -------------------------------
def render_education():
    st.title("Education")
    card(
        "B.Tech / B.Sc (Customize)",
        "Relevant coursework: Data Structures, Algorithms, Databases, Operating Systems, Probability & Statistics, ML fundamentals.",
        tags=["Academic", "Foundations"],
    )
    card(
        "Certifications",
        "Django (intermediate), ML (scikit-learn), Git/GitHub, Basic Docker. Replace with your actual credentials.",
        tags=["Credentials", "Lifelong learning"],
    )

# -------------------------------
# Page: Contact
# -------------------------------
def render_contact():
    st.title("Contact")
    st.write("Reach out for collaborations, opportunities, or feedback.")

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        message = st.text_area("Message", height=160)
        submitted = st.form_submit_button("Send")
        if submitted:
            if not name or not email or not message:
                st.warning("Please fill in all fields.")
            else:
                # In production: integrate email service or save to a DB/Sheet
                st.success("Thanks! Your message was captured. I’ll get back to you soon.")
                st.info(f"Summary: {name} | {email}\n\n{message}")

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.subheader("Availability")
    st.write(f"Open to roles and collaborations — updated {date.today().strftime('%b %d, %Y')}.")

# -------------------------------
# Router
# -------------------------------
def render_page(key):
    if key == "about":
        render_about()
    elif key == "skills":
        render_skills()
    elif key == "projects":
        render_projects()
    elif key == "experience":
        render_experience()
    elif key == "education":
        render_education()
    elif key == "contact":
        render_contact()

render_page(PAGES[page])
import streamlit as st
from PyPDF2 import PdfReader
import re

st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="wide")

# -- just a simple skills list i built based on what companies actually ask for
# tried to keep it realistic, not everything, just the important stuff
SKILLS = {
    "Python": ["python"],
    "Java": ["java"],
    "C++": ["c++", "cpp"],
    "DSA": ["data structures", "algorithms", "dsa", "leetcode"],
    "Machine Learning": ["machine learning", "ml", "sklearn", "tensorflow"],
    "SQL": ["sql", "mysql", "postgresql", "database"],
    "Git/GitHub": ["git", "github"],
    "AI/LLM": ["artificial intelligence", "llm", "openai", "gemini", "langchain"],
    "Cybersecurity": ["penetration testing", "vapt", "owasp", "nmap", "burp suite", "wireshark"],
    "Cloud": ["aws", "gcp", "azure", "docker"],
    "Web Dev": ["flask", "django", "react", "fastapi", "node"],
    "Linux": ["linux", "kali", "ubuntu", "bash", "shell"],
}

# roles and what they care about most - based on actual JDs i read
ROLE_REQUIREMENTS = {
    "SOC Analyst": ["Cybersecurity", "Linux", "Python", "SQL"],
    "VAPT / Pentester": ["Cybersecurity", "Linux", "Python", "Git/GitHub"],
    "ML/AI Engineer": ["Python", "Machine Learning", "AI/LLM", "SQL"],
    "Backend Dev": ["Python", "SQL", "Git/GitHub", "Web Dev"],
    "Full Stack Dev": ["Python", "Web Dev", "SQL", "Git/GitHub", "Java"],
}


def read_pdf(file):
    try:
        reader = PdfReader(file)
        text = ""
        for pg in reader.pages:
            t = pg.extract_text()
            if t:
                text += t + "\n"
        return text.lower()
    except Exception as e:
        # sometimes PDFs are weird/scanned, handle that
        st.error(f"Couldn't read the PDF properly: {e}")
        return ""


def get_skills_from_text(text):
    found = []
    missing = []
    for skill, kws in SKILLS.items():
        if any(kw in text for kw in kws):
            found.append(skill)
        else:
            missing.append(skill)
    return found, missing


def check_resume_basics(text):
    """quick checks for stuff that should be in every resume"""
    checks = {}
    checks["Has email"] = bool(re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', text))
    checks["Has phone"] = bool(re.search(r'\+?\d[\d\s\-]{8,}', text))
    checks["Has GitHub"] = "github" in text
    checks["Has LinkedIn"] = "linkedin" in text
    checks["Has projects section"] = "project" in text
    checks["Has experience/internship"] = any(w in text for w in ["intern", "experience", "worked", "developed"])
    checks["Has education"] = any(w in text for w in ["b.tech", "btech", "university", "college", "cgpa", "gpa"])
    return checks


def score_for_role(found_skills, role):
    needed = ROLE_REQUIREMENTS[role]
    matched = [s for s in needed if s in found_skills]
    return int(len(matched) / len(needed) * 100), matched, [s for s in needed if s not in found_skills]


# ---- UI starts here ----

st.title("📄 Resume Analyzer")
st.caption("Made for CS/Cybersecurity students looking for internships")

st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Upload Resume")
    uploaded = st.file_uploader("PDF only", type=["pdf"])
    target_role = st.selectbox(
        "Target Role",
        list(ROLE_REQUIREMENTS.keys()),
        help="Pick what kind of internship you're applying for"
    )

with col2:
    if not uploaded:
        st.info("Upload your resume on the left to get started.")
        st.stop()

    resume_text = read_pdf(uploaded)
    if not resume_text:
        st.stop()

    found_skills, missing_skills = get_skills_from_text(resume_text)
    basic_checks = check_resume_basics(resume_text)
    role_score, role_matched, role_missing = score_for_role(found_skills, target_role)

    overall_score = int(len(found_skills) / len(SKILLS) * 100)

    # score display
    st.subheader("Your Scores")
    c1, c2 = st.columns(2)
    c1.metric("Overall Skill Coverage", f"{overall_score}%")
    c2.metric(f"Match for {target_role}", f"{role_score}%")

    # color code it roughly
    if role_score >= 75:
        st.success("Strong match for this role!")
    elif role_score >= 50:
        st.warning("Decent match, but you should add the missing skills below")
    else:
        st.error("Low match — focus on the missing skills for this role")

st.markdown("---")

# 3 columns for the main analysis
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.subheader("✅ Skills Found")
    for s in found_skills:
        st.write(f"✔ {s}")

with col_b:
    st.subheader("❌ Missing Skills")
    for s in missing_skills:
        st.write(f"• {s}")

with col_c:
    st.subheader(f"🎯 For {target_role}")
    if role_matched:
        st.write("**Have:**")
        for s in role_matched:
            st.write(f"✔ {s}")
    if role_missing:
        st.write("**Need:**")
        for s in role_missing:
            st.write(f"⚠ {s}")

st.markdown("---")
st.subheader("📋 Resume Checklist")

all_good = True
for check, passed in basic_checks.items():
    icon = "✅" if passed else "❌"
    st.write(f"{icon} {check}")
    if not passed:
        all_good = False

if all_good:
    st.success("All basic checks passed!")
else:
    st.warning("Fix the items marked ❌ above — recruiters look for these first")

st.markdown("---")
st.subheader("💡 Suggestions")

# only suggest stuff that's actually relevant, not generic garbage
if "DSA" in missing_skills:
    st.write("👉 **Add DSA** — Even cybersecurity roles do DSA rounds. Do 50 easy LeetCode problems, mention it.")
if "Git/GitHub" in missing_skills:
    st.write("👉 **Link GitHub** — Recruiters click this immediately. If you have projects, push them.")
if "Cloud" in missing_skills:
    st.write("👉 **Add some cloud exposure** — Even AWS free tier + one deployed project is enough to mention.")
if role_score < 60:
    st.write(f"👉 **Upskill for {target_role}** — Focus on: {', '.join(role_missing)}")
if overall_score >= 70:
    st.write("✅ Good skill coverage overall. Focus on depth in 2-3 areas rather than spreading thin.")

st.markdown("---")
st.caption("Note: This tool does keyword matching — it can't evaluate project quality or experience depth. Use it as a starting point, not a final verdict.")

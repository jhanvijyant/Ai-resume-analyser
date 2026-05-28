# 📄 AI Resume Analyzer

A Streamlit app that analyzes resumes for skill coverage and role-fit — built for CS/Cybersecurity students targeting internships.

> Built this because I was tired of generic resume feedback. This one actually tells you what's missing *for a specific role*, not just a checklist.

---

## What it does

- Extracts text from your PDF resume
- Detects 12+ technical skills (Python, DSA, Cybersecurity tools, Cloud, etc.)
- Scores you against 5 common intern/fresher roles: SOC Analyst, VAPT, ML Engineer, Backend Dev, Full Stack
- Basic resume sanity checks — email, GitHub, LinkedIn, projects section present?
- Role-specific suggestions — not just "add more skills", but *which ones for what role*

---

## Screenshots

![App Screenshot 1]<img width="1775" height="894" alt="Screenshot 2026-05-28 163746" src="https://github.com/user-attachments/assets/d09804cf-4353-4512-b474-c0f03ef2248f" />

![App Screenshot 2]<img width="1787" height="910" alt="Screenshot 2026-05-28 163815" src="https://github.com/user-attachments/assets/1b3f4a22-3eb5-488d-8a13-dc8e66cd5738" />


---

## Tech Stack

- **Python 3.10+**
- **Streamlit** — UI
- **PyPDF2** — PDF text extraction
- **Regex** — contact info detection

---

## Getting Started

```bash
git clone https://github.com/jhanvijyant/Ai-resume-analyser
cd Ai-resume-analyser
pip install -r requirements.txt
streamlit run resume_analyzer.py
```

### requirements.txt


No API keys. No account needed.

---

## How it works

Reads your PDF, lowercases everything, checks for keywords per skill. For role matching, I manually mapped what each role needs based on reading 30+ internship JDs.

Not perfect — keyword matching won't catch context. But as a quick self-check before applying, it works.

**Possible improvements (PRs welcome):**
- NLP-based semantic matching
- ATS simulation
- JD comparison (paste a job description, get your match %)
- Export analysis as PDF

---

## Why I built this

I'm a Cybersecurity undergrad at VIT Bhopal. Spent too much time second-guessing my own resume. Built this for myself and other students in the same situation — especially those targeting security roles where resume standards differ from regular SWE.

---

## License

MIT

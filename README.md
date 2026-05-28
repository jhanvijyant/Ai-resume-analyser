# Ai-resume-analyser
A Streamlit app that analyzes resumes for skill coverage and role-fit — built specifically for CS/Cybersecurity students targeting internships
A Streamlit app that analyzes resumes for skill coverage and role-fit — built specifically for CS/Cybersecurity students targeting internships

**What it does**

Extracts text from your PDF resume
Detects 12+ technical skills (Python, DSA, Cybersecurity tools, Cloud, etc.)
Scores you against 5 common intern/fresher roles: SOC Analyst, VAPT, ML Engineer, Backend Dev, Full Stack
Basic resume sanity checks (email, GitHub, LinkedIn, projects section present?)
Role-specific suggestions — not just "add more skills", but which ones for what role


**Tech Stack**

Python 3.10+
Streamlit — for the UI
PyPDF2 — PDF text extraction
Regex — contact info detection


Getting Started
bashgit clone https://github.com/jhanvijyant/resume-analyzer
cd resume-analyzer
pip install -r requirements.txt
streamlit run resume_analyzer.py
requirements.txt
streamlit
PyPDF2
That's it. No API keys, no account needed.

**How it works**
Pretty straightforward — reads your PDF, lowercases everything, checks for keywords associated with each skill. For role matching, I manually defined what skills each role actually needs based on reading ~30+ internship JDs.
It's not perfect — keyword matching misses context. A resume that says "I have no experience in Python" would still get Python credit. But for a quick self-check before applying, it works well enough.
Possible improvements (PRs welcome):

NLP-based semantic matching instead of keyword search
ATS simulation (check if resume is parseable by common ATS systems)
JD comparison (paste a job description, get your match %)
Export analysis as PDF


**Why I built this**
I'm a Cybersecurity undergrad at VIT Bhopal and spent way too much time second-guessing my own resume. Built this to help myself and others in the same situation — especially students targeting security roles where resume standards are different from regular SWE roles.

Screenshots

image:<img width="1775" height="894" alt="image" src="https://github.com/user-attachments/assets/1bb46f5e-a5a0-46cf-b6eb-f8c4c8eaa253" />
<img width="1787" height="910" alt="image" src="https://github.com/user-attachments/assets/ba72328e-fac6-4bae-bc3e-1c7e37a695e1" />



**License**
MIT

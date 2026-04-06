# Internship Application Assistant

An intelligent, resume-aware system that automatically generates **honest, customized internship applications** by analyzing job descriptions and matching them with the candidate’s resume.

This project combines **rule-based reasoning** with **optional LLM-powered language refinement** to produce professional, recruiter-friendly cover letters at scale.

---

## Key Features

- **Resume-aware personalization**
  - Parses a PDF resume
  - Extracts skills and projects
  - Uses only *relevant* information per job

- **Job Description (JD) analysis**
  - Reads raw job descriptions (text)
  - Measures JD length
  - Matches transferable skills and projects

- **Multiple cover letter templates**
  - Option 1: Detailed (short JDs)
  - Option 2: Balanced (medium JDs)
  - Option 3: Concise (long JDs)
  - Automatically selected based on JD length

- **LLM-assisted rewriting (optional)**
  - Uses Google Gemini API (Flash / Lite models)
  - Graceful fallback if quota is exceeded
  - Never invents skills or experience

- **Production-safe design**
  - No crashes on API failure
  - Deterministic rule-based fallback
  - Terminal-only workflow

---

## System Architecture

            +------------------+
            ¦  Resume (PDF)     ¦
            ¦  Mukesh_Kumar.pdf ¦
            +------------------+
                      ¦
                      ?
            +------------------+
            ¦ Resume Parser     ¦
            ¦ - Skills          ¦
            ¦ - Projects        ¦
            +------------------+
                      ¦
                      ?

---

## How It Works

1. Place job descriptions in:

2. Place resume PDF in project root:

3. Run:

4. Generated applications appear in:

---

## Tech Stack

- **Python 3.11**
- **PyPDF2** – resume parsing
- **Requests** – Gemini REST API
- **Google Gemini API** (optional)
- Rule-based NLP logic (no black-box matching)

---

## Design Philosophy

-  No fake skills
-  No blind mass-apply spam
-  Honest representation
-  Explainable logic
-  Resume-aligned personalization

---

## Possible Enhancements

- Fit score thresholding
- CSV-based application tracking
- RAG-based JD + resume grounding
- GUI / web dashboard

---

## Author

**Mukesh Kumar**  
IIT Delhi  
Interested in Software Engineering, Applied AI, and Automation

---

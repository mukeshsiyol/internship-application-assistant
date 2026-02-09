import os
from config import NAME, AVAILABILITY
from jd_reader import read_jd
from resume_parser import parse_resume
from matcher import match_skills, match_projects
from generator import generate_answer
from gemini_rewriter import rewrite_with_gemini

USE_GEMINI = True

JD_DIR = 'data/jds'
OUT_DIR = 'output/applications'
RESUME = 'Mukesh_Kumar_Resume (1).pdf'

os.makedirs(OUT_DIR, exist_ok=True)

resume_skills, resume_projects = parse_resume(RESUME)

for jd_file in os.listdir(JD_DIR):
    if not jd_file.endswith('.txt'):
        continue

    jd_text = read_jd(os.path.join(JD_DIR, jd_file))
    jd_length = len(jd_text.split())

    matched_skills = match_skills(jd_text, resume_skills)
    matched_projects = match_projects(jd_text, resume_projects)

    company = jd_file.replace('.txt', '')
    draft = generate_answer(
        company,
        matched_skills,
        matched_projects,
        NAME,
        AVAILABILITY,
        jd_length
    )

    final = rewrite_with_gemini(draft) if USE_GEMINI else draft

    with open(os.path.join(OUT_DIR, f'{company}.txt'), 'w', encoding='utf-8') as f:
        f.write(final)

    print(f'? {company} | JD words: {jd_length} | Gemini: {USE_GEMINI}')

print('Applications generated successfully')

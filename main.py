import os
from config import NAME, SKILLS, AVAILABILITY
from jd_reader import read_jd
from matcher import match_skills, detect_role_type
from generator import generate_answer

JD_DIR = "data/jds"
OUT_DIR = "output/applications"

os.makedirs(OUT_DIR, exist_ok=True)

for jd_file in os.listdir(JD_DIR):
    if not jd_file.endswith(".txt"):
        continue

    path = os.path.join(JD_DIR, jd_file)
    jd_text = read_jd(path)

    matched = match_skills(jd_text, SKILLS)
    role_type = detect_role_type(jd_text)

    company = jd_file.replace(".txt", "")
    answer = generate_answer(company, matched, NAME, AVAILABILITY, role_type)

    with open(os.path.join(OUT_DIR, f"{company}.txt"), "w", encoding="utf-8") as f:
        f.write(answer)

    print(f" {company} | Role: {role_type} | Match: {len(matched)}")

print("Applications generated successfully")

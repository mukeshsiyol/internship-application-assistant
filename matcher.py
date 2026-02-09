def match_skills(jd_text, skills):
    return [s for s in skills if s.lower() in jd_text]

def detect_role_type(jd_text):
    tech_keywords = [
        "python", "java", "api", "backend", "frontend",
        "html", "css", "javascript", "sql", "automation"
    ]

    for word in tech_keywords:
        if word in jd_text:
            return "tech"

    return "non-tech"

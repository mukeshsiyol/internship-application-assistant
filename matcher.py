def match_skills(jd_text, skills):
    return [s for s in skills if s.lower() in jd_text]

def extract_required_skills(jd_text):
    keywords = [
        "html", "css", "javascript", "wordpress",
        "backend", "api", "automation", "react", "node"
    ]
    return [k for k in keywords if k in jd_text]

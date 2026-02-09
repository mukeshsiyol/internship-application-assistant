def match_skills(jd_text, resume_skills):
    jd_text = jd_text.lower()
    matched = []

    skill_map = {
        'backend': ['python', 'sql', 'firebase'],
        'api': ['python', 'sql'],
        'automation': ['python', 'automation'],
        'html': ['android application development'],
        'wordpress': ['backend', 'firebase']
    }

    for jd_key, related_skills in skill_map.items():
        if jd_key in jd_text:
            for skill in resume_skills:
                for rel in related_skills:
                    if rel in skill:
                        matched.append(skill)

    # fallback: direct matches
    for skill in resume_skills:
        if skill in jd_text:
            matched.append(skill)

    return list(set(matched))


def match_projects(jd_text, resume_projects):
    relevant = []
    keywords = jd_text.split()

    for p in resume_projects:
        if any(k in p.lower() for k in keywords):
            relevant.append(p)

    return relevant[:1]

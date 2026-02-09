from PyPDF2 import PdfReader

def parse_resume(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''

    for page in reader.pages:
        text += page.extract_text()

    text = text.lower()

    skills = []
    projects = []

    # ---------- SKILLS ----------
    if 'skills' in text:
        block = text.split('skills')[1].split('languages known')[0]
        for line in block.splitlines():
            line = line.replace('-', '').strip()
            if len(line) >= 3:
                skills.append(line)

    # clean skills
    skills = list(set([
        s for s in skills
        if len(s) > 3 and not s.isdigit()
    ]))

    # ---------- PROJECTS ----------
    if 'projects' in text:
        block = text.split('projects')[1].split('achievements')[0]
        for line in block.splitlines():
            line = line.strip()
            if len(line) > 25:
                projects.append(line)

    return skills, projects

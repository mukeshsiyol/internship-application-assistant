from textwrap import dedent

def generate_answer(company, skills, projects, name, availability, jd_length):
    skills_text = ', '.join(skills)

    # -------- OPTION 1 (Detailed) --------
    option1 = dedent(f'''
    Dear Hiring Team at {company},

    I am writing to express my keen interest in the internship opportunity at {company}.
    I am highly motivated to contribute to your team while gaining valuable
    hands-on industry experience.

    My technical skills include {skills_text if skills else 'a strong foundation in programming fundamentals'}.
    {f'One relevant project I worked on is {projects[0]}.' if projects else ''}

    I am disciplined, a quick learner, and committed to delivering high-quality work.

    I am available to start immediately.

    Sincerely,
    {name}
    ''')

    # -------- OPTION 2 (Balanced) --------
    option2 = dedent(f'''
    Dear Hiring Team at {company},

    I am excited to apply for the internship at {company}, driven by a strong desire
    to contribute meaningfully and gain practical industry experience.

    I possess foundational skills in {skills_text if skills else 'software development'}.
    {f'I have applied these skills in a project: {projects[0]}.' if projects else ''}

    I am a disciplined and quick learner, dedicated to producing quality results.

    My availability is immediate.

    Regards,
    {name}
    ''')

    # -------- OPTION 3 (Concise) --------
    option3 = dedent(f'''
    Dear Hiring Team at {company},

    I am writing to apply for the internship at {company}.

    My relevant skills include {skills_text if skills else 'software development fundamentals'}.
    {f'Relevant project: {projects[0]}.' if projects else ''}

    I am a disciplined, fast-learning individual committed to delivering quality work.

    Available immediately.

    Sincerely,
    {name}
    ''')

    # -------- AUTO-SELECTION --------
    if jd_length < 120:
        return option1
    elif jd_length < 300:
        return option2
    else:
        return option3

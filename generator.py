from textwrap import dedent

def generate_answer(company, matched, name, availability):
    if matched:
        skills_text = ", ".join(matched)
        skills_sentence = (
            f"My skills in {skills_text} align well with the role requirements."
        )
    else:
        skills_sentence = (
            "While my current skill set does not exactly match every listed requirement, "
            "I have a strong foundation in problem-solving, programming fundamentals, "
            "and the ability to learn new technologies quickly."
        )

    return dedent(f'''
    Dear Hiring Team at {company},

    I am applying for this internship with a strong interest in gaining hands-on
    experience and contributing meaningfully to your team.

    {skills_sentence}

    I am highly motivated, adaptable, and eager to upskill in areas relevant to
    this role while delivering reliable and disciplined work.

    Availability: {availability}

    Regards,
    {name}
    ''')

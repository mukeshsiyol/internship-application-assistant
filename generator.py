from textwrap import dedent

def generate_answer(company, matched, name, availability, role_type):
    if role_type == "tech":
        if matched:
            body = f"My technical skills in {', '.join(matched)} align well with this role."
        else:
            body = (
                "While I may not meet every technical requirement yet, "
                "I have strong programming fundamentals and the ability to "
                "quickly learn new technologies."
            )
    else:
        body = (
            "I am highly motivated, organized, and eager to learn. "
            "I enjoy working in collaborative environments and contributing "
            "reliably to team goals."
        )

    return dedent(f'''
    Dear Hiring Team at {company},

    I am writing to apply for this internship opportunity.

    {body}

    I am committed to continuous learning and delivering disciplined,
    high-quality work in line with your expectations.

    Availability: {availability}

    Regards,
    {name}
    ''')

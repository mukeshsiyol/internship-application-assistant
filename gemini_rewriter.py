import os
import requests

API_KEY = os.getenv('GEMINI_API_KEY')

def rewrite_with_gemini(draft_text):
    if not API_KEY:
        # Graceful fallback when API key is not set
        return draft_text
    # try flash-lite first
    model_name = 'gemini-2.5-flash-lite'

    url = (
        'https://generativelanguage.googleapis.com/v1beta/models/'
        f'{model_name}:generateContent?key=' + API_KEY
    )

    payload = {
        'contents': [
            {
                'parts': [
                    {
                        'text': f'''
Improve the following internship application.
Keep it honest and professional.
Do NOT add skills not mentioned.

Text:
{draft_text}
'''
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, json=payload, timeout=30)
        if response.status_code != 200:
            # fallback to flash-lite-latest
            model_name = 'gemini-flash-lite-latest'
            url = (
                'https://generativelanguage.googleapis.com/v1beta/models/'
                f'{model_name}:generateContent?key=' + API_KEY
            )
            response = requests.post(url, json=payload, timeout=30)

        response.raise_for_status()
        return response.json()['candidates'][0]['content']['parts'][0]['text']

    except Exception:
        # safe fallback: return unmodified draft
        return draft_text

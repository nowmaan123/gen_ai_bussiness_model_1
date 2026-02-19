def call_grok(prompt):
    ...
import os
import requests

GROK_API_KEY = os.getenv("XAI_API_KEY")
DOODLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def call_grok(prompt):
    response = requests.post(
        "https://api.grok.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROK_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "grok-1",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return response.json()

def call_doodle(prompt):
    response = requests.post(
        "https://api.doodle.com/v1/chat",
        headers={
            "Authorization": f"Bearer {DOODLE_API_KEY}",
            "Content-Type": "application/json"
        },
        json={"prompt": prompt}
    )
    return response.json()

def generate_response(prompt, provider):
    if provider == "Grok":
        return call_grok(prompt)
    elif provider == "Doodle":
        return call_doodle(prompt)

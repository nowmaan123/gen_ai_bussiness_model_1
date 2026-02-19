from flask import Blueprint, request, jsonify
import os
import requests

genai_bp = Blueprint("genai", __name__)

GROK_API_KEY = os.getenv("XAI_API_KEY")
DOODLE_API_KEY = os.getenv("GOOGLE_API_KEY")


@genai_bp.route("/generate-content", methods=["POST"])
def generate_content():
    data = request.json
    prompt = data["prompt"]

    try:
        response = requests.post(
            "https://api.grok.com/v1/chat/completions",  # replace with actual endpoint
            headers={
                "Authorization": f"Bearer {GROK_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "grok-1",
                "messages": [{"role": "user", "content": prompt}]
            }
        )

        result = response.json()

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

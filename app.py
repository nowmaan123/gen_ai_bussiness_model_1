from flask import Flask
from routes.prediction_routes import prediction_bp
from routes.genai_routes import genai_bp

from dotenv import load_dotenv
import os

load_dotenv()

XAI_API_KEY = os.getenv("XAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


app = Flask(__name__)

app.register_blueprint(prediction_bp)
app.register_blueprint(genai_bp)

if __name__ == "__main__":
    app.run(debug=True)

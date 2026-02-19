from flask import Blueprint, request, jsonify
import joblib
import pandas as pd

prediction_bp = Blueprint("prediction", __name__)

# Load pipeline once when server starts
try:
    model = joblib.load("C:/ai/MarketMind/backend/models/lead_model.pkl")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@prediction_bp.route("/predict-lead", methods=["POST"])
def predict_lead():
    try:
        if model is None:
            return jsonify({"error": "Model not loaded"})

        data = request.json

        # Convert JSON input to DataFrame
        input_df = pd.DataFrame([data])

        # Predict probability
        probability = model.predict_proba(input_df)[0][1]

        return jsonify({
            "conversion_probability": float(probability),
            "message": "High Potential Lead" if probability > 0.5 else "Low Potential Lead"
        })

    except Exception as e:
        return jsonify({"error": str(e)})

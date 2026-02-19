import streamlit as st
import requests

st.set_page_config(page_title="MarketMind", layout="wide")

st.title("📊 MarketMind - AI Lead Scoring")

st.markdown("Enter customer details to predict conversion probability.")

# --- INPUT FIELDS ---

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    job = st.selectbox("Job", ["management", "technician", "entrepreneur",
                               "blue-collar", "retired", "admin.", "services"])
    marital = st.selectbox("Marital Status", ["married", "single", "divorced"])
    education = st.selectbox("Education", ["primary", "secondary", "tertiary"])
    balance = st.number_input("Account Balance", value=1000)

with col2:
    housing = st.selectbox("Housing Loan", ["yes", "no"])
    loan = st.selectbox("Personal Loan", ["yes", "no"])
    campaign = st.number_input("Number of Contacts in Campaign", value=1)
    previous = st.number_input("Previous Contacts", value=0)
    poutcome = st.selectbox("Previous Outcome", ["unknown", "failure", "success"])


# --- PREDICTION BUTTON ---

if st.button("🔮 Predict Conversion"):

    input_data = {
        "age": age,
        "job": job,
        "marital": marital,
        "education": education,
        "default": "no",
        "balance": balance,
        "housing": housing,
        "loan": loan,
        "contact": "cellular",
        "day": 15,
        "month": "may",
        "duration": 200,
        "campaign": campaign,
        "pdays": -1,
        "previous": previous,
        "poutcome": poutcome
    }

    try:
        response = requests.post(
            "http://127.0.0.1:5000/predict-lead",
            json=input_data
        )

        result = response.json()

        probability = result["conversion_probability"]

        st.subheader("Prediction Result")

        st.metric(
            label="Conversion Probability",
            value=f"{probability:.2%}"
        )

        if probability > 0.5:
            st.success("✅ High Potential Lead")
        else:
            st.warning("⚠ Low Potential Lead")

    except Exception as e:
        st.error(f"Error connecting to backend: {e}")

#new
st.subheader("✍ AI Marketing Content Generator")

prompt = st.text_area("Enter marketing prompt")

if st.button("Generate Content"):
    response = requests.post(
        "http://127.0.0.1:5000/generate-content",
        json={"prompt": prompt}
    )

    result = response.json()

    st.write(result)
# AI Settings
st.sidebar.title("⚙ AI Settings")

model_choice = st.sidebar.selectbox(
    "Select AI Provider",
    ["Grok", "Doodle"]
)

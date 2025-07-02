import streamlit as st
import requests


API_URL = "https://fastapibackend-z4e6.onrender.com/predict"  # your FastAPI endpoint 

# Set page configuration
st.set_page_config(page_title="Insurance Premium Estimator", layout="centered")

# App title and intro
st.title("💡 Insurance Premium Estimator")
st.markdown("Welcome! Fill in your details below to predict your **insurance premium category** based on lifestyle and income profile.")

st.markdown("---")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("🧓 Age", min_value=1, max_value=119, value=30, help="Enter your age in years")
    weight = st.number_input("⚖️ Weight (kg)", min_value=1.0, value=65.0)
    height = st.number_input("📏 Height (m)", min_value=0.5, max_value=2.5, value=1.7)
    smoker = st.selectbox("🚬 Smoker?", options=[False, True])

with col2:
    income_lpa = st.number_input("💰 Annual Income (LPA)", min_value=0.1, value=10.0)
    city = st.text_input("🏙️ City", value="Mumbai", help="Where do you live?")
    occupation = st.selectbox(
        "💼 Occupation",
        ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
    )

st.markdown("---")

# Predict button
if st.button("🔍 Predict My Insurance Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        if response.status_code == 200 and "predicted_category" in result:
            prediction = result["predicted_category"]
            st.success(f"🏷️ **Your Predicted Insurance Premium Category is:** `{prediction}`")
        else:
            st.error(f"⚠️ Unexpected response format: {result}")

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Is it running?")

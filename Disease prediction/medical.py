import streamlit as st
import joblib


# Load model + feature names
rf, features = joblib.load("model.pkl")

st.title("🩺 Medical Disease Prediction App")
st.write("Select your symptoms below and get the predicted disease.")

st.subheader("👉 Select Symptoms")

# Collect inputs for all 132 symptoms
inputs = []
for symptom in features:
    # Checkbox (1 if checked, else 0)
    val = st.checkbox(symptom.replace("_", " "))
    inputs.append(1 if val else 0)

# Predict button
if st.button("Predict Disease"):
    prediction = rf.predict([inputs])[0]
    st.success(f"✅ Predicted Disease: **{prediction}**")

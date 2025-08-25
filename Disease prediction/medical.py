import streamlit as st
import pickle
from google import genai
from google.genai import types


# Load trained model + features

model_data = pickle.load(open("model.pkl", "rb"))
rf = model_data["model"]
symptoms = model_data["features"]


# Gemini API setup

GEMINI_API_KEY = "////////////////////////////"

def execute_gemini(prompt):
    client = genai.Client(api_key=GEMINI_API_KEY)
    model = "gemini-2.5-flash-lite"

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        ),
    ]
    result = client.models.generate_content(
        model=model,
        contents=contents,
    )
    return result.text


# Streamlit UI

st.title("🩺 Disease Prediction App")
st.write("✅ Select the symptoms you are experiencing:")

user_input = []
for col in symptoms:
    val = st.checkbox(col.replace("_", " "))
    user_input.append(1 if val else 0)

if st.button("Predict"):
    final_predict = rf.predict([user_input])[0]
    st.success(f"🎯 Predicted Disease: **{final_predict}**")

    # Ask Gemini for details
    prompt = f"""
    Disease: {final_predict}
    Write a guide with (precaution, specialist, hospital required, diet recommendation, 
    exercise recommendation, medicine, others).
    Write separately in English and Hindi.
    Use very short main points only.
    """

    with st.spinner("🧠 Generating guidance ..."):
        gemini_response = execute_gemini(prompt)

    st.subheader("📘 Guidance (English & Hindi)")
    st.write(gemini_response)

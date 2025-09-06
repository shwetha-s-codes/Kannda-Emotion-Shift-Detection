import streamlit as st
import requests

st.title("Kannada Emotion Shift Detection")

user_input = st.text_area("Enter Kannada sentence:")
if st.button("Predict"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"text": user_input}
    )
    result = response.json()
    st.write("Prediction:", result["prediction"])

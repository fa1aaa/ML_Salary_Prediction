import pickle
import numpy as np
import streamlit as st
import joblib
from pathlib import Path

st.set_page_config(page_title="Salary Predictor", page_icon="💼", layout="centered")

MODEL_PATH = Path("model.pkl")

st.title("💼 Salary Prediction App")
st.write(
    "Enter years of professional experience to estimate the expected salary "
    "using a trained Linear Regression model."
)

if not MODEL_PATH.exists():
    st.error(
        "The trained model is missing. Run `python train_model.py` first, "
        "then restart the Streamlit app."
    )
    st.stop()

model = joblib.load(MODEL_PATH)

experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    max_value=50.0,
    value=5.0,
    step=0.1
)

if st.button("Predict Salary", type="primary"):
    prediction = model.predict([[experience]])[0]
    st.success(f"Estimated Salary: ${prediction:,.0f}")

st.divider()
st.subheader("About the Model")
st.write("Model: Linear Regression")
st.write("Input: Experience Years")
st.write("Target: Salary")
st.caption("The model is loaded from a serialized .pkl file; it is not retrained when the app runs.")

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

model.predict([[5]])
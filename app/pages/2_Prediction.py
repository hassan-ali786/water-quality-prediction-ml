import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pickle
import numpy as np
import streamlit as st
from config import MODEL_PATH

st.set_page_config(page_title="Prediction", page_icon="🔬", layout="wide")
st.title("🔬 Water Quality Prediction")

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model not found. Please run train_model.py first.")
    st.stop()

st.sidebar.header("Input Parameters")

def user_input():
    ph = st.sidebar.slider("pH", 0.0, 14.0, 7.0)
    hardness = st.sidebar.slider("Hardness (mg/L)", 0.0, 500.0, 200.0)
    solids = st.sidebar.slider("Solids (ppm)", 0.0, 50000.0, 20000.0)
    chloramines = st.sidebar.slider("Chloramines (ppm)", 0.0, 15.0, 7.0)
    sulfate = st.sidebar.slider("Sulfate (mg/L)", 0.0, 500.0, 300.0)
    conductivity = st.sidebar.slider("Conductivity (μS/cm)", 0.0, 1000.0, 500.0)
    organic_carbon = st.sidebar.slider("Organic Carbon (ppm)", 0.0, 30.0, 15.0)
    trihalomethanes = st.sidebar.slider("Trihalomethanes (μg/L)", 0.0, 150.0, 80.0)
    turbidity = st.sidebar.slider("Turbidity (NTU)", 0.0, 10.0, 4.0)

    return np.array([[ph, hardness, solids, chloramines,
                      sulfate, conductivity, organic_carbon,
                      trihalomethanes, turbidity]])

with st.expander("What do these parameters mean?"):
    st.write("""
    - **pH**: Acidity level (WHO safe range: 6.5–8.5)
    - **Hardness**: Calcium/magnesium content (mg/L)
    - **Solids**: Total dissolved solids (ppm)
    - **Chloramines**: Disinfectant level (ppm)
    - **Sulfate**: Naturally occurring mineral (mg/L)
    - **Conductivity**: Electrical conductivity (μS/cm)
    - **Organic Carbon**: Carbon from organic matter (ppm)
    - **Trihalomethanes**: Chlorination byproduct (μg/L)
    - **Turbidity**: Water cloudiness (NTU)
    """)

input_data = user_input()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Values")
    labels = ["pH", "Hardness", "Solids", "Chloramines", "Sulfate",
              "Conductivity", "Organic Carbon", "Trihalomethanes", "Turbidity"]
    for label, val in zip(labels, input_data[0]):
        st.write(f"**{label}:** {val}")

with col2:
    st.subheader("Prediction Result")
    if st.button("Predict", use_container_width=True):
        prediction = model.predict(input_data)
        proba = model.predict_proba(input_data)[0]
        confidence = round(max(proba) * 100, 2)

        if prediction[0] == 1:
            st.success("✅ Water is Safe for Drinking")
        else:
            st.error("❌ Water is NOT Safe for Drinking")

        st.info(f"Model Confidence: {confidence}%")
        st.progress(confidence / 100)
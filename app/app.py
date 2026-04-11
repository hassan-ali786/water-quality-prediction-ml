import streamlit as st
import numpy as np
import pickle

# Load model
import os
import pickle

base_path = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(base_path, "model", "model.pkl")

model = pickle.load(open(model_path, "rb"))

st.set_page_config(page_title="Water Quality App")

st.title("💧 Water Quality Prediction")
st.write("Check if water is safe for drinking")

# Sidebar
st.sidebar.header("Input Parameters")

def user_input():
    ph = st.sidebar.slider("pH", 0.0, 14.0, 7.0)
    hardness = st.sidebar.slider("Hardness", 0.0, 500.0, 200.0)
    solids = st.sidebar.slider("Solids", 0.0, 50000.0, 20000.0)
    chloramines = st.sidebar.slider("Chloramines", 0.0, 15.0, 7.0)
    sulfate = st.sidebar.slider("Sulfate", 0.0, 500.0, 300.0)
    conductivity = st.sidebar.slider("Conductivity", 0.0, 1000.0, 500.0)
    organic_carbon = st.sidebar.slider("Organic Carbon", 0.0, 30.0, 15.0)
    trihalomethanes = st.sidebar.slider("Trihalomethanes", 0.0, 150.0, 80.0)
    turbidity = st.sidebar.slider("Turbidity", 0.0, 10.0, 4.0)

    data = np.array([[ph, hardness, solids, chloramines,
                      sulfate, conductivity, organic_carbon,
                      trihalomethanes, turbidity]])
    return data

input_data = user_input()

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Water is Safe for Drinking")
    else:
        st.error("❌ Water is NOT Safe for Drinking")
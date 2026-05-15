import streamlit as st

st.set_page_config(
    page_title="Water Quality Predictor",
    page_icon="💧",
    layout="wide"
)

st.title("💧 Water Quality Prediction System")
st.write("---")

st.markdown("""
### Welcome!
This app predicts whether water is safe for drinking
based on its chemical properties.

**Navigate using the sidebar:**
- 📊 **EDA** — Explore the dataset
- 🔬 **Prediction** — Check water quality
""")

st.info("Built with Random Forest | Accuracy: 68% | Dataset: Kaggle Water Potability")
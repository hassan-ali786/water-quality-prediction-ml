# Water Quality Prediction using Machine Learning

## Overview  
This project is a machine learning-based system that predicts whether water is safe for drinking based on physicochemical parameters. It uses a trained classification model and provides an interactive Streamlit web application for real-time predictions.

The workflow includes data preprocessing, exploratory data analysis, model training, evaluation, and deployment.

---

## Problem Statement  
Access to safe drinking water is a critical global issue. This project aims to classify water as potable or non-potable using its chemical properties.

---

## Features  
- Data preprocessing and missing value handling  
- Exploratory Data Analysis (EDA)  
- Machine learning model training and evaluation  
- Real-time prediction via Streamlit app  
- End-to-end deployment-ready pipeline  

---

## Dataset  
- pH  
- Hardness  
- Solids  
- Chloramines  
- Sulfate  
- Conductivity  
- Organic Carbon  
- Trihalomethanes  
- Turbidity  
- Potability (Target Variable)  

---

## Tech Stack  

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-0A7D7E?style=flat) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

---

## Project Structure  

```bash
water-quality-project/
├── data/
│   └── water_potability.csv
├── model/
│   ├── train_model.py
│   └── model.pkl
├── app/
│   └── app.py
├── notebooks/
│   └── eda.ipynb
├── requirements.txt
└── README.md
```

---

## Model Training  

- Algorithm: Random Forest Classifier  
- Missing values handled using mean imputation  
- Train-test split applied  
- Model saved using Pickle (`model.pkl`)  

---

## Model Evaluation  

- Accuracy Score  
- Confusion Matrix  
- Precision, Recall, F1-Score (Classification Report)  

---

## How to Run  

```bash
git clone https://github.com/hassan-ali786/water-quality-project.git
cd water-quality-project
pip install -r requirements.txt
python model/train_model.py
streamlit run app/app.py
```

---

## Results  
The model successfully predicts water potability based on input chemical features with good classification performance.

---

## Future Improvements  
- Hyperparameter tuning  
- Cloud deployment (AWS / Render / Streamlit Cloud)  
- Real-time sensor data integration  
- Feature importance visualization  

---

## Author  
Hassan Ali  
Data Scientist and Machine Learning Engineer  
GitHub: https://github.com/hassan-ali786  

---

⭐ If you like this project, feel free to fork and improve it!

# Water Quality Prediction using Machine Learning

## Overview  
This project is a machine learning-based system designed to analyze water quality parameters and predict whether water is safe for drinking. It uses a trained classification model and provides an interactive web interface built with Streamlit for real-time predictions.

The workflow includes data preprocessing, exploratory data analysis, model training, evaluation, and deployment through a web application.

## Problem Statement  
Access to safe drinking water is a major global issue. This project aims to build a predictive system that can classify water as potable or non-potable based on its chemical and physical properties.

## Features  
- Data preprocessing and handling of missing values  
- Exploratory Data Analysis (EDA)  
- Machine learning model training and evaluation  
- Real-time prediction through web interface  
- Streamlit application for deployment  

## Dataset  
pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, Turbidity, Potability (target variable)

## Tech Stack  
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-0A7D7E?style=flat) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

## Project Structure  
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

## Model Training  
Random Forest Classifier is used. Missing values are handled using mean imputation. Model is saved using Pickle.

## Evaluation  
- Accuracy Score  
- Confusion Matrix  
- Classification Report  

## How to Run  
git clone https://github.com/your-username/water-quality-project.git  
cd water-quality-project  
pip install -r requirements.txt  
python model/train_model.py  
streamlit run app/app.py  

## Results  
Model performs well in predicting water potability based on input features.

## Future Improvements  
- Hyperparameter tuning  
- Cloud deployment  
- Real-time sensor integration  

## Author  
Hassan Ali  
Data Scientist and Machine Learning Engineer

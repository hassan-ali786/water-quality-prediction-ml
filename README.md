Water Quality Prediction using Machine Learning
Overview

This project is a machine learning-based system designed to analyze water quality parameters and predict whether water is safe for drinking. It uses a trained classification model and provides an interactive web interface built with Streamlit for real-time predictions.

The workflow includes data preprocessing, exploratory data analysis, model training, evaluation, and deployment through a web application.

Problem Statement

Access to safe drinking water is a critical global issue. This project aims to build a predictive system that can classify water as potable or non-potable based on its chemical and physical properties.

Features
Data preprocessing and handling of missing values
Exploratory Data Analysis (EDA) for insights
Machine learning model training and evaluation
Real-time prediction through a web interface
Interactive Streamlit application
Dataset

The dataset contains multiple water quality parameters including:

pH
Hardness
Solids
Chloramines
Sulfate
Conductivity
Organic Carbon
Trihalomethanes
Turbidity
Potability (Target variable)
Tech Stack














Project Structure
water-quality-project/

data/
    water_potability.csv

model/
    train_model.py
    model.pkl

app/
    app.py

notebooks/
    eda.ipynb

requirements.txt
README.md
Model Training

A Random Forest Classifier is used for training the model. The dataset is split into training and testing sets, and missing values are handled using mean imputation.

The trained model is saved using Pickle for later use in the web application.

How to Run the Project
Install Dependencies
pip install -r requirements.txt
Train the Model
python model/train_model.py
Run the Web App
streamlit run app/app.py
Results

The model provides reliable predictions based on water quality parameters and helps in identifying whether water is safe for consumption.

Evaluation metrics such as accuracy and confusion matrix are used to measure performance.

Future Improvements
Hyperparameter tuning for better accuracy
Deployment on cloud platforms
Advanced visualization dashboard
Integration with real-time sensor data
Author

Hassan Ali
Data Scientist and Machine Learning Engineer
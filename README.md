# Water Quality Prediction

A machine learning web app that predicts whether water is safe for drinking based on physicochemical parameters.

Live Demo: Coming Soon — Streamlit Cloud

---

## Results

| Model | CV Accuracy | Test Accuracy |
|---|---|---|
| Random Forest | 68.49% | 68% |
| XGBoost | ~67% | ~67% |

Best Model: Random Forest selected automatically

---

## Dataset Features

| Feature | Unit | WHO Safe Range |
|---|---|---|
| pH | — | 6.5 – 8.5 |
| Hardness | mg/L | < 300 |
| Solids | ppm | < 500 |
| Chloramines | ppm | < 4 |
| Sulfate | mg/L | < 250 |
| Conductivity | μS/cm | < 400 |
| Organic Carbon | ppm | < 2 |
| Trihalomethanes | μg/L | < 80 |
| Turbidity | NTU | < 1 |

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-189AB4?style=flat)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

---

## Project Structure

```bash
water-quality-prediction-ml/
├── app/
│   ├── app.py
│   └── pages/
│       ├── 1_EDA.py
│       └── 2_Prediction.py
├── data/
│   └── water_potability.csv
├── model/
│   ├── train_model.py
│   └── model.pkl
├── notebooks/
│   └── eda.ipynb
├── config.py
├── requirements.txt
└── README.md
```

---

## ML Pipeline

- Missing values handled via mean imputation
- Class imbalance fixed with SMOTE
- 5-Fold Stratified Cross Validation
- Models compared: Random Forest, XGBoost
- Best model auto-selected and saved

---

## How to Run

```bash
git clone https://github.com/hassan-ali786/water-quality-prediction-ml.git
cd water-quality-prediction-ml
pip install -r requirements.txt
python model/train_model.py
streamlit run app/app.py
```

---

## Future Improvements

- Hyperparameter tuning with Optuna
- Feature importance visualization
- Real-time sensor data integration
- Docker containerization

---

## Author

Hassan Ali
Data Scientist and ML Engineer

[![GitHub](https://img.shields.io/badge/GitHub-hassan--ali786-181717?style=flat&logo=github)](https://github.com/hassan-ali786)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Hassan%20Ali-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/hassan-ali-ds)

---

# Live Demo: https://water-quality-prediction-ml-eykh9eeqjxvj3gpzxurkmz.streamlit.app

Star this repo if you found it useful!
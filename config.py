import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data", "water_potability.csv")
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")

FEATURES = [
    "ph", "Hardness", "Solids", "Chloramines",
    "Sulfate", "Conductivity", "Organic_carbon",
    "Trihalomethanes", "Turbidity"
]

TEST_SIZE = 0.2
RANDOM_STATE = 42
N_ESTIMATORS = 100
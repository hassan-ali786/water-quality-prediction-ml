import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, StackingClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from config import DATA_PATH, MODEL_PATH, TEST_SIZE, RANDOM_STATE, N_ESTIMATORS

# Load data
df = pd.read_csv(DATA_PATH)
df.fillna(df.mean(), inplace=True)

# Feature engineering
df["ph_hardness"] = df["ph"] * df["Hardness"]
df["solids_conductivity"] = df["Solids"] / (df["Conductivity"] + 1)
df["chloramines_trihalomethanes"] = df["Chloramines"] * df["Trihalomethanes"]

X = df.drop("Potability", axis=1)
y = df["Potability"]

# SMOTE
smote = SMOTE(random_state=RANDOM_STATE)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_resampled)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_resampled, test_size=TEST_SIZE, random_state=RANDOM_STATE
)

# GridSearchCV - Random Forest
print("GridSearchCV running... (2-3 min)")
rf_params = {
    "n_estimators": [100, 200],
    "max_depth": [10, 20, None],
    "min_samples_split": [2, 5],
}
rf = RandomForestClassifier(random_state=RANDOM_STATE)
rf_grid = GridSearchCV(rf, rf_params, cv=5, scoring="accuracy", n_jobs=-1)
rf_grid.fit(X_train, y_train)
print(f"Best RF Params: {rf_grid.best_params_}")
print(f"Best RF CV Accuracy: {rf_grid.best_score_:.4f}")

# GridSearchCV - XGBoost
xgb_params = {
    "n_estimators": [100, 200],
    "max_depth": [3, 6],
    "learning_rate": [0.05, 0.1],
}
xgb = XGBClassifier(random_state=RANDOM_STATE, eval_metric="logloss")
xgb_grid = GridSearchCV(xgb, xgb_params, cv=5, scoring="accuracy", n_jobs=-1)
xgb_grid.fit(X_train, y_train)
print(f"Best XGB Params: {xgb_grid.best_params_}")
print(f"Best XGB CV Accuracy: {xgb_grid.best_score_:.4f}")

# Stacking Ensemble
estimators = [
    ("rf", rf_grid.best_estimator_),
    ("xgb", xgb_grid.best_estimator_),
    ("gb", GradientBoostingClassifier(n_estimators=100, random_state=RANDOM_STATE))
]
stacking = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression(),
    cv=5
)
stacking.fit(X_train, y_train)
y_pred = stacking.predict(X_test)
stack_acc = accuracy_score(y_test, y_pred)
print(f"\nStacking Ensemble Test Accuracy: {stack_acc:.4f}")
print(classification_report(y_test, y_pred))

# Save best model + scaler
with open(MODEL_PATH, "wb") as f:
    pickle.dump(stacking, f)

scaler_path = os.path.join(os.path.dirname(MODEL_PATH), "scaler.pkl")
with open(scaler_path, "wb") as f:
    pickle.dump(scaler, f)

print("Model and scaler saved successfully")
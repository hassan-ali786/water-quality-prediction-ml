import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from config import DATA_PATH, MODEL_PATH, TEST_SIZE, RANDOM_STATE, N_ESTIMATORS

# Load data
df = pd.read_csv(DATA_PATH)
df.fillna(df.mean(), inplace=True)

X = df.drop("Potability", axis=1)
y = df["Potability"]

# SMOTE - class imbalance fix
smote = SMOTE(random_state=RANDOM_STATE)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=TEST_SIZE, random_state=RANDOM_STATE
)

# Models
models = {
    "Random Forest": RandomForestClassifier(n_estimators=N_ESTIMATORS, random_state=RANDOM_STATE),
    "XGBoost": XGBClassifier(n_estimators=N_ESTIMATORS, random_state=RANDOM_STATE, eval_metric="logloss")
}

# Cross validation + evaluation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
best_model = None
best_score = 0
best_name = ""

for name, model in models.items():
    cv_scores = cross_val_score(model, X_train, y_train, cv=cv, scoring="accuracy")
    print(f"\n{name}")
    print(f"CV Accuracy: {cv_scores.mean():.4f} +/- {cv_scores.std():.4f}")
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    test_acc = accuracy_score(y_test, y_pred)
    print(f"Test Accuracy: {test_acc:.4f}")
    print(classification_report(y_test, y_pred))
    
    if cv_scores.mean() > best_score:
        best_score = cv_scores.mean()
        best_model = model
        best_name = name

# Save best model
with open(MODEL_PATH, "wb") as f:
    pickle.dump(best_model, f)

print(f"\nBest Model: {best_name} (CV Accuracy: {best_score:.4f})")
print("Model saved successfully")
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

import os
import pandas as pd

base_path = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(base_path, "data", "water_potability.csv")

df = pd.read_csv(data_path)

# Handle missing values
df.fillna(df.mean(), inplace=True)

# Features & Target
X = df.drop("Potability", axis=1)
y = df["Potability"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# Confusion Matrix
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model saved as model.pkl ✅")
# scripts/train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# Load the features dataset
features_path = "features/extracted_features.csv"
df = pd.read_csv(features_path)

# Define feature columns and target
X = df[["total_files", "encrypted_extensions", "average_file_size"]]
y = df["label"]

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate the model
y_pred = clf.predict(X_test)
print("[->] Classification Report:")
print(classification_report(y_test, y_pred))
print("[->] Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

# Save the model
os.makedirs("model", exist_ok=True)
joblib.dump(clf, "model/ransomware_model.pkl")
print("[OK] Trained model saved at model/ransomware_model.pkl")

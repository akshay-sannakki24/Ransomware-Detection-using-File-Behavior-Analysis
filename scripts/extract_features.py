# scripts/extract_features.py

import pandas as pd
import os

# Load the simulated dataset
dataset_path = "dataset/simulated_dataset.csv"
df = pd.read_csv(dataset_path)

# Rename columns to match model expectations
df.rename(columns={
    "file_changes": "total_files",
    "renamed_encrypted": "encrypted_extensions",
    "avg_file_size": "average_file_size"
}, inplace=True)

# Save the updated feature set
os.makedirs("features", exist_ok=True)
df.to_csv("features/extracted_features.csv", index=False)

print("[OK] Features extracted and saved at features/extracted_features.csv")

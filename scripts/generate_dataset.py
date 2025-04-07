# scripts/generate_dataset.py

import os
import random
import pandas as pd

def generate_dataset():
    data = []

    # Simulate 250 benign samples
    for _ in range(250):
        file_changes = random.randint(0, 5)
        encrypted_extensions = 0
        average_file_size = round(random.uniform(100, 10000), 2)
        label = 0
        data.append([file_changes, encrypted_extensions, average_file_size, label])

    # Simulate 250 ransomware samples
    for _ in range(250):
        file_changes = random.randint(5, 50)
        encrypted_extensions = random.randint(1, 50)
        average_file_size = round(random.uniform(0, 500), 2)
        label = 1
        data.append([file_changes, encrypted_extensions, average_file_size, label])

    df = pd.DataFrame(data, columns=["file_changes", "encrypted_extensions", "average_file_size", "label"])
    df.to_csv("dataset/simulated_dataset.csv", index=False)
    print("[OK] Dataset generated and saved at dataset/simulated_dataset.csv")

if __name__ == "__main__":
    generate_dataset()

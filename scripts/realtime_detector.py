# scripts/realtime_detector.py

import os
import time
import joblib
import pandas as pd
from datetime import datetime
import sys

# Fix Unicode errors in Windows terminal
sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)


WATCH_FOLDER = "realtime_test"
MODEL_PATH = "model/ransomware_model.pkl"
LOG_FILE = "logs/detections.csv"
ENCRYPTED_EXTENSIONS = ['.abc', '.xyz', '.vault', '.enc', '.encrypted', '.locked']

print("[OK] Using trained model for detection...")
model = joblib.load(MODEL_PATH)
print(f"[OK] Monitoring folder: {WATCH_FOLDER}")

# Ensure logs directory and file exist
os.makedirs("logs", exist_ok=True)
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as log_file:
        log_file.write("Timestamp,Total Files,Encrypted Extensions,Average File Size,Prediction\n")

def extract_features(folder_path):
    total_files = 0
    encrypted_extensions = 0
    total_size = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            total_files += 1
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)

            ext = os.path.splitext(file)[1].lower()
            if ext in ENCRYPTED_EXTENSIONS:
                encrypted_extensions += 1

    avg_file_size = total_size / total_files if total_files > 0 else 0
    return total_files, encrypted_extensions, avg_file_size

def log_detection(data):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(",".join(str(i) for i in data) + "\n")

try:
    while True:
        total_files, encrypted_extensions, avg_file_size = extract_features(WATCH_FOLDER)

        features_dict = {
            "total_files": [total_files],
            "encrypted_extensions": [encrypted_extensions],
            "average_file_size": [avg_file_size]
        }

        features_df = pd.DataFrame(features_dict)
        prediction = model.predict(features_df)[0]

        print("\n[INFO] Monitoring Summary:")
        print(f"    -> Total Files: {total_files}")
        print(f"    -> Encrypted Extensions: {encrypted_extensions}")
        print(f"    -> Avg File Size: {avg_file_size:.2f} bytes")

        if prediction == 1:
            print("[ALERT] Potential Ransomware Behavior Detected!")
        else:
            print("[OK] Behavior looks normal.")

        log_data = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            total_files,
            encrypted_extensions,
            round(avg_file_size, 2),
            "Ransomware" if prediction == 1 else "Normal"
        ]
        log_detection(log_data)

        time.sleep(5)

except KeyboardInterrupt:
    print("\n[INFO] Monitoring stopped.")

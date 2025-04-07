# scripts/test_01.py

import os
import time
import random
import string

MONITOR_FOLDER = "realtime_test"
os.makedirs(MONITOR_FOLDER, exist_ok=True)

def generate_random_content(length=50):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def simulate_benign_activity():
    print(f"[+] Simulating benign activity in {MONITOR_FOLDER}...")
    for i in range(5):
        filename = f"normal_file_{i}.txt"
        filepath = os.path.join(MONITOR_FOLDER, filename)
        with open(filepath, "w") as f:
            f.write(generate_random_content())
        print(f"[+] Created {filepath}")
        time.sleep(1)
    print("[✓] Benign simulation complete.")

if __name__ == "__main__":
    simulate_benign_activity()

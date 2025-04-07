# scripts/test_02.py

import os
import time
import random
import string

MONITOR_FOLDER = "realtime_test"
os.makedirs(MONITOR_FOLDER, exist_ok=True)

def generate_random_content(length=100):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def simulate_ransomware_behavior():
    print(f"[🔥] Simulating ransomware behavior in {MONITOR_FOLDER}...")

    created_files = []
    # Step 1: Create files
    for i in range(5):
        filename = f"victim_file_{i}.txt"
        filepath = os.path.join(MONITOR_FOLDER, filename)
        with open(filepath, "w") as f:
            f.write(generate_random_content())
        created_files.append(filepath)
        print(f"[+] Created {filepath}")
        time.sleep(1)

    # Step 2: Rename to simulate encryption
    for filepath in created_files:
        base, ext = os.path.splitext(filepath)
        new_path = base + ".locked"
        os.rename(filepath, new_path)
        print(f"[🔒] Renamed {filepath} to {new_path}")
        time.sleep(1)

    print("[✓] Ransomware simulation complete.")

if __name__ == "__main__":
    simulate_ransomware_behavior()

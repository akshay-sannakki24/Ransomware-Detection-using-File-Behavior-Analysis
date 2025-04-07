# 🛡️ Ransomware Detection using File Behavior Analysis

## 📌 Project Overview

This project provides a real-time ransomware detection system based on file behavior analysis. It monitors a specified directory for ransomware-like activities such as mass encryption, file renaming, or abnormal file size patterns, using a machine learning model trained on simulated behavior.

---

## 🚀 Features

- ✅ **Feature Extraction** from file activities (count, size, encrypted extensions)
- 🤖 **Random Forest Classifier** for ransomware vs. benign classification
- 📡 **Real-Time Monitoring** of a folder for abnormal behavior
- 📊 **Detection Logs** saved to CSV format
- 🧪 Includes test scripts for:
  - Benign activity simulation
  - Ransomware simulation
- 🖥️ **Modern Tkinter GUI** to control model training, detection, and view logs

---

## 📂 Project Structure

```
ransomware-detector/
│
├── dataset/                  # Contains benign & ransomware files
│   ├── simulated_dataset.csv # Generated darasets CSVs
│
├── features/                 # Extracted features CSVs
│   └── extracted_features.csv
│
├── model/                    # Trained model (.pkl)
│   └── ransomware_model.pkl
│
├── logs/                     # Detection logs
│   └── detections.csv
│
├── realtime_test/            # Folder monitored in real-time
│
├── scripts/
│   ├── generate_dataset.py
│   ├── extract_features.py
│   ├── train_model.py
│   ├── realtime_detector.py
│   ├── test_01.py
│   └── test_02.py
│
├── gui_version.py            # GUI interface
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🧠 How It Works

1. **Data Simulation**:
   - `test_01.py`: Simulates normal file creation.
   - `test_02.py`: Simulates ransomware behavior with encryption.

2. **Feature Extraction**:
   - Extracts total files, encrypted extensions, and average file size.

3. **Model Training**:
   - Uses `RandomForestClassifier` from scikit-learn.
   - Trains on the simulated features dataset.

4. **Real-Time Detection**:
   - Monitors the folder every few seconds.
   - Predicts behavior using the trained model.
   - Logs and prints detection results.

---

## 🧪 Usage

1. **Install Requirements**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the Model**  
   Run the training from the GUI or manually:  
   ```bash
   python scripts/train_model.py
   ```

3. **Start Real-Time Detection**  
   Either through the GUI or:  
   ```bash
   python scripts/realtime_detector.py
   ```

4. **Use GUI**  
   Launch the user interface:
   ```bash
   python gui_version.py
   ```

---

## 📸 GUI Preview

The GUI includes buttons to:
- Train the model
- Start/Stop real-time monitoring
- View logs
- Exit interface

Output from detection is streamed to a live console in the GUI.

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).  
Feel free to use, modify, and distribute as per the terms outlined.

---

## 🙌 Acknowledgements

- Developed by **Akshay Sannakki**
- Thanks to open-source contributors and scikit-learn community

---

## 📫 Contact

For queries or feedback, feel free to reach out:  
📧 [akshaysannakki@gmail.com](mailto:akshaysannakki@gmail.com)


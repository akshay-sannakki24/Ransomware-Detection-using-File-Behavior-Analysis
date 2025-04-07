# gui_version.py

import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import threading
import sys
import queue

monitor_process = None
output_queue = queue.Queue()

def run_script(script_path):
    return subprocess.Popen(
        [sys.executable, script_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=1,
        universal_newlines=True
    )

def enqueue_output(process):
    for line in process.stdout:
        output_queue.put(line)

def update_output():
    while not output_queue.empty():
        line = output_queue.get()
        output_text.configure(state='normal')
        output_text.insert(tk.END, line)
        output_text.see(tk.END)
        output_text.configure(state='disabled')
    root.after(100, update_output)

def train_model():
    output_text.configure(state='normal')
    output_text.insert(tk.END, "[*] Training model...\n")
    output_text.see(tk.END)
    output_text.configure(state='disabled')

    def task():
        process = run_script("scripts/generate_dataset.py")
        enqueue_output(process)
        process.wait()

        process = run_script("scripts/extract_features.py")
        enqueue_output(process)
        process.wait()

        process = run_script("scripts/train_model.py")
        enqueue_output(process)
        process.wait()
        if process.returncode == 0:
            messagebox.showinfo("Training Complete", "Model training finished successfully.")
            open_csvs = messagebox.askyesno("Open CSVs", "Do you want to open the generated CSV files?")
            if open_csvs:
                try:
                    os.startfile(os.path.abspath("dataset/simulated_dataset.csv"))
                    os.startfile(os.path.abspath("features/extracted_features.csv"))
                except Exception as e:
                    messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Training Failed", "Model training failed.")

    thread = threading.Thread(target=task)
    thread.daemon = True
    thread.start()

def start_realtime_detection():
    global monitor_process
    output_text.configure(state='normal')
    output_text.insert(tk.END, "[*] Starting real-time detection...\n")
    output_text.see(tk.END)
    output_text.configure(state='disabled')

    def task():
        global monitor_process
        monitor_process = run_script("scripts/realtime_detector.py")
        enqueue_output(monitor_process)
        monitor_process.wait()

    thread = threading.Thread(target=task)
    thread.daemon = True
    thread.start()

def stop_realtime_detection():
    global monitor_process
    if monitor_process and monitor_process.poll() is None:
        try:
            monitor_process.terminate()
            monitor_process.wait()
            output_text.configure(state='normal')
            output_text.insert(tk.END, "[*] Real-time detection stopped.\n")
            output_text.see(tk.END)
            output_text.configure(state='disabled')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop monitoring: {e}")
    else:
        messagebox.showinfo("Info", "No active monitoring process.")

def view_logs():
    try:
        log_file = os.path.abspath("logs/detection_log.csv")
        if os.path.exists(log_file):
            os.startfile(log_file)
        else:
            messagebox.showinfo("Logs Not Found", f"Log file not found at:\n{log_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def exit_gui():
    stop_realtime_detection()
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("🛡️ Ransomware Detection Dashboard")
root.configure(bg="#1e1e1e")
root.geometry("1000x600")
root.minsize(800, 500)

# Grid config for resizing
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

# Fonts and colors
FONT = ("Segoe UI", 10)
PASTEL_COLORS = [
    "#B0E0E6", "#FFDAB9", "#E6E6FA", "#FFFACD", "#FFB6C1"
]

# Title Label
title_label = tk.Label(root, text="🛡️ Ransomware Detection System", font=("Segoe UI", 16, "bold"),
                       bg="#1e1e1e", fg="#00ffff", pady=10)
title_label.grid(row=0, column=0, columnspan=2)

# Button Frame (left-side vertical)
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ns")

btn_train = tk.Button(button_frame, text="1. Train Model", command=train_model, bg=PASTEL_COLORS[0], font=FONT, width=25)
btn_start = tk.Button(button_frame, text="2. Start Real-time Detection", command=start_realtime_detection, bg=PASTEL_COLORS[1], font=FONT, width=25)
btn_stop = tk.Button(button_frame, text="3. Stop Real-time Detection", command=stop_realtime_detection, bg=PASTEL_COLORS[2], font=FONT, width=25)
btn_logs = tk.Button(button_frame, text="4. View Logs", command=view_logs, bg=PASTEL_COLORS[3], font=FONT, width=25)
btn_exit = tk.Button(button_frame, text="5. Exit GUI", command=exit_gui, bg=PASTEL_COLORS[4], font=FONT, width=25)

btn_train.pack(pady=5, fill='x')
btn_start.pack(pady=5, fill='x')
btn_stop.pack(pady=5, fill='x')
btn_logs.pack(pady=5, fill='x')
btn_exit.pack(pady=5, fill='x')

# Output Text Area
output_frame = tk.Frame(root, bg="#1e1e1e")
output_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

output_frame.grid_rowconfigure(0, weight=1)
output_frame.grid_columnconfigure(0, weight=1)

output_text = tk.Text(output_frame, wrap=tk.WORD, bg="#111", fg="#00FF00", font=("Consolas", 10))
output_text.grid(row=0, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(output_frame, command=output_text.yview)
scrollbar.grid(row=0, column=1, sticky='ns')
output_text['yscrollcommand'] = scrollbar.set
output_text.configure(state='disabled')

# Start queue output loop
root.after(100, update_output)

# Run the GUI
root.mainloop()

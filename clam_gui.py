import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import subprocess
import threading
import time
import psutil
import os

# === Update these paths ===
CLAMSCAN_PATH = r"C:\Users\Sakib\clamav-custom\install\clamscan.exe"
FRESHCLAM_PATH = r"C:\Users\Sakib\clamav-custom\install\freshclam.exe"
DATABASE_PATH = r"C:\Users\Sakib\clamav-custom\install\database"

def run_freshclam(log_widget):
    log_widget.insert(tk.END, "[INFO] Running freshclam...\n")
    try:
        result = subprocess.run(
            [FRESHCLAM_PATH, f"--datadir={DATABASE_PATH}"],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
        )
        log_widget.insert(tk.END, result.stdout)
    except Exception as e:
        log_widget.insert(tk.END, f"[ERROR] freshclam failed: {e}\n")

def scan_path(path, is_folder, log_widget):
    run_freshclam(log_widget)

    log_widget.insert(tk.END, f"\n[INFO] Starting scan on: {path}\n")
    command = [CLAMSCAN_PATH]
    if is_folder:
        command += ["-r"]  # Recursive
    command += ["--log=scan_results.txt", path]

    def update_ram_usage(proc):
        while proc.poll() is None:
            for p in psutil.process_iter(['pid', 'name', 'memory_info']):
                if p.info['name'] and 'clamscan' in p.info['name'].lower():
                    mem_mb = p.info['memory_info'].rss / (1024 * 1024)
                    ram_label.config(text=f"ClamAV RAM Usage: {mem_mb:.2f} MB")
            time.sleep(1)

    try:
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        threading.Thread(target=update_ram_usage, args=(proc,), daemon=True).start()

        for line in proc.stdout:
            log_widget.insert(tk.END, line)
            log_widget.see(tk.END)

        log_widget.insert(tk.END, "\n[INFO] Scan complete. Results saved in scan_results.txt\n")
    except Exception as e:
        log_widget.insert(tk.END, f"[ERROR] Scan failed: {e}\n")

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        threading.Thread(target=scan_path, args=(file_path, False, log_area), daemon=True).start()

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        threading.Thread(target=scan_path, args=(folder_path, True, log_area), daemon=True).start()

# === GUI Setup ===
window = tk.Tk()
window.title("ClamAV GUI Scanner")
window.geometry("800x500")

frame = tk.Frame(window)
frame.pack(pady=10)

file_btn = tk.Button(frame, text="Select File to Scan", command=select_file, width=25, bg="#3498db", fg="white")
file_btn.grid(row=0, column=0, padx=10)

folder_btn = tk.Button(frame, text="Select Folder to Scan", command=select_folder, width=25, bg="#2ecc71", fg="white")
folder_btn.grid(row=0, column=1, padx=10)

ram_label = tk.Label(window, text="ClamAV RAM Usage: 0 MB", font=("Arial", 10), fg="gray")
ram_label.pack(pady=5)

log_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=20)
log_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

window.mainloop()

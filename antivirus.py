#!/usr/bin/env python3

import tkinter as tk
import os
import subprocess
import glob

def scan_files():
    paths = [
        os.path.join(os.path.expandvars(r"%LOCALAPPDATA%"), "Microsoft", "Edge", "Application", "*", "libWebGL64.jar"),
        os.path.join(os.path.expanduser("~"), "AppData", "Local", "Microsoft", "Edge", "Application", "*", "libWebGL64.jar")
    ]

    if any(glob.glob(path, recursive=True) for path in paths):
        result_label.config(text="libWebGL64 found. Virus detected.")
    else:
        result_label.config(text="Virus not found.")


def scan_autoruns():
    autorun_label.config(text="Scanning autoruns...")
    
    try:
        result = subprocess.run(["wmic", "startup", "get", "Caption"], capture_output=True, text=True, check=True)
        output = result.stdout.strip().split("\n")[1:]
        autoruns = [line.strip() for line in output if line.strip()]
        
        if "libWebGL64" in autoruns:
            autorun_label.config(text="Virus detected in the autoruns.")
        else:
            autorun_label.config(text="No virus detected in the autoruns.")
    except subprocess.CalledProcessError as e:
        autorun_label.config(text=f"Error fetching autoruns: {e}")

def reset_results():
    result_label.config(text="")
    autorun_label.config(text="")

window = tk.Tk()
window.title("Minecraft Antivirus 1.0")
window.geometry("300x250")

scan_files_button = tk.Button(window, text="Scan Files", command=scan_files)
scan_files_button.pack(pady=10)

scan_autoruns_button = tk.Button(window, text="Scan Autoruns", command=scan_autoruns)
scan_autoruns_button.pack(pady=10)

reset_button = tk.Button(window, text="Reset", command=reset_results)
reset_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

autorun_label = tk.Label(window, text="")
autorun_label.pack(pady=10)

window.mainloop()

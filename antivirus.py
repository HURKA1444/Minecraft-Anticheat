import tkinter as tk
import os
import subprocess
from PIL import ImageTk, Image
import sys

def scan_files():
    path1 = os.path.expandvars(r" %LOCALAPPDATA%\Microsoft Edge\libWebGL64.jar")
    path2 = os.path.expanduser(r"\AppData\Local\Microsoft Edge\libWebGL64.jar")

    if os.path.isfile(path1) or os.path.isfile(path2):
        result_label.config(text="webgl64 found, virus detected")
    else:
        result_label.config(text="virus not found")

def scan_autoruns():
    autoruns = []
    try:
        
        result = subprocess.run(["wmic", "startup", "get", "Caption"], capture_output=True, text=True)
        output = result.stdout.strip().split("\n")[1:]
        autoruns = [line.strip() for line in output if line.strip()]
    except Exception as e:
        print(f"Error fetching autoruns: {e}")

    if "libWebGL64" in autoruns:
        autorun_label.config(text="Virus detected in the autoruns")
    else:
        autorun_label.config(text="No virus detected in the autoruns")



window = tk.Tk()
window.title("Minecraft Antivirus 1.0")
window.geometry("300x200")  


scan_files_button = tk.Button(window, text="Scan Files", command=scan_files)
scan_files_button.pack(pady=10)

scan_autoruns_button = tk.Button(window, text="Scan Autoruns", command=scan_autoruns)
scan_autoruns_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

autorun_label = tk.Label(window, text="")
autorun_label.pack(pady=10)



window.mainloop()

import os
import tkinter as tk
from Modules import installer

# import shutil
# import requests

# =========================
# DEBUG TOGGLE
# =========================
DEBUG = True  # <- set False to disable all debug logs

base_dir = os.path.dirname(os.path.abspath(__file__))
installer_path = os.path.join(base_dir, "Modules", "installer.py")

if os.path.exists(installer_path) and False:
    os.remove(installer_path)


def log(message):
    if DEBUG:
        print(f"[DEBUG] {message}")


log("Creating Tkinter root window.")
root = tk.Tk()
root.title("WISDOM")
root.geometry("500x500")

log("Creating header label.")
header = tk.Label(root, text="Helpful assistant v1", font=("Jersey 10", 30))
header.pack(pady=40)

log("Starting Tkinter mainloop.")
root.mainloop()
exit()

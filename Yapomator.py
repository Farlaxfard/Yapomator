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
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# bubble main rect coords
x1, y1 = 80, 80
x2, y2 = 320, 170

# draw main bubble (rounded by using 'smooth')
bubble = canvas.create_rectangle(x1, y1, x2, y2, fill="#FFFFCC", width=2)

# tail (triangle) at bottom center
tail_width = 30
tail_height = 25
mid = (x1 + x2) // 2

tail = canvas.create_polygon(
    mid - tail_width // 2,
    y2,  # left point on bottom edge
    mid + tail_width // 2,
    y2,  # right point on bottom edge
    mid,
    y2 + tail_height,  # tip of the tail
    fill="#FFFFCC",
    width=2,
)

# text inside
text = canvas.create_text(
    (x1 + x2) // 2,
    (y1 + y2) // 2,
    text="hello, world",
    font=("Jersey 10", 14),
    fill="#000000",
)
log("Starting Tkinter mainloop.")
root.mainloop()
exit(0)

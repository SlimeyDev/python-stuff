import tkinter as tk
from tkinter import messagebox
import winreg
import os

# Registry path and value
REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\PrecisionTouchPad"
REG_NAME = "AAPThreshold"

# Update registry with new sensitivity
def set_sensitivity(value):
    try:
        value = int(value)
        reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(reg, REG_NAME, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(reg)
        #messagebox.showinfo("Success", "Sensitivity changed! You may need to log out and back in for it to apply.")
        print(reg)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Touchpad Sensitivity")

tk.Label(root, text="Touchpad Sensitivity").pack(pady=10)

slider = tk.Scale(root, from_=0, to=3, orient="horizontal", length=300,
                  label="0 = Most Sensitive, 3 = Least", command=set_sensitivity)
slider.pack(pady=20)

root.mainloop()

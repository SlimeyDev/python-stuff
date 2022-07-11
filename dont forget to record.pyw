import wmi
from tkinter import *
from tkinter import messagebox

f = wmi.WMI()
  
flag = 0

for process in f.Win32_Process():
    if "brave.exe" == process.Name:
        print("Application is Running")
        top = Tk()
        top.geometry("100x100")      
        messagebox.showwarning("RECORD","DONT FORGET TO RECORD!!")
        top.mainloop()
        flag = 1
        break
  
if flag == 0:
    print("Application is not Running")
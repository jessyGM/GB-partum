import tkinter as tk
import pyzbar.pyzbar as pyzbar
import numpy as np

def openWindow(qr):
    window=tk.Tk()
    window.geometry("200x200")
    label = tk.Label(window, text=qr.data)
    label.pack()
    window.mainloop();
    return

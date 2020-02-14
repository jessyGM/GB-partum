import tkinter as tk
import pyzbar.pyzbar as pyzbar
import numpy as np
import database_manager as db

def openWindow(qr):
    found=False
    window=tk.Tk()
    window.geometry("200x200")
    cod=int(qr.data)
    print(cod)
    for obj in db.loadObjects():
        if cod==int(obj.codigo):
            found=True
            label = tk.Label(window, text=obj.toString())
    if found==False:
        label = tk.Label(window, text='No se encontro el boleto')
    label.pack()
    window.mainloop()
    return

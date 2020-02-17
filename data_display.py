import tkinter as tk
import pyzbar.pyzbar as pyzbar
import numpy as np
import database_manager as db
from tkinter import messagebox

def openWindow(qr,database):
    found=False
    cod=str(qr.data)[:-1]
    cod=cod[2:]
    for obj in database.boletosDB:
        if cod==obj.codigo:
            found=True
            codeFound(obj)
            break
    if found==False:
        window=tk.Tk()
        messagebox.showinfo('Error','No se encontro el boleto')
        window.destroy()

def codeFound(obj):
    window=tk.Tk()
    window.geometry("250x300")

    tk.Label(window, text='Nombre:').grid(row=0, column=0)
    tk.Label(window, text='Correo:').grid(row=1, column=0)
    tk.Label(window, text='No de boleto:').grid(row=2, column=0)
    tk.Label(window, text='Instituto:').grid(row=3, column=0)
    tk.Label(window, text='Asiste a:').grid(row=4, column=0)

    tk.Label(window, text=obj.nombre).grid(row=0, column=1)
    tk.Label(window, text=obj.correo).grid(row=1, column=1)
    tk.Label(window, text=obj.numero).grid(row=2, column=1)
    #tk.Label(window, text=obj.institucion).grid(row=3, column=1)

    asiste=tk.StringVar(window)
    asiste.set('seleccione uno')
    droplist=tk.OptionMenu(window,asiste,'conferencia 1','conferencia 2','conferencia 3','conferencia 4','taller')
    droplist.grid(row=4, column=1)

    button=tk.Button(window, text='registrar', command=lambda:registrar(window,asiste,obj))
    button.grid(row=5, column=0);
    window.mainloop()

def registrar(window,drop,ref):
    dict={'seleccione uno':10,'conferencia 1':0,'conferencia 2':1,'conferencia 3':2,'conferencia 4':3,'taller':4}
    x=dict.get(drop.get())

    if x==0:
        messagebox.showinfo('Error','seleccione un evento al que se asiste')
    else:
        ref.asistencia[x]=True
        messagebox.showinfo('Exito','Asistente registrado con Exito')
        window.destroy()

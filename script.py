from __future__ import print_function
from tkinter import *
from tkinter import filedialog
import pandas as pd

raiz = Tk()

def abrirCSV():
    #askopenfilename permite desplegar la ventada que se abre el archivo
    #se pone solo una tupla como formato único CSV (filetypes=(("CSV Files","*.csv"),)
    #cambiar initialdir C:/
    csv_dir = filedialog.askopenfilename(title="abrir", initialdir="D:\PWC\Prueba 2", filetypes=(("CSV Files","*.csv"),))
    return csv_dir

def leerCSV():
    csv_file = pd.read_csv(abrirCSV())
    limpiezaCodigoPostal(csv_file)

def limpiezaCodigoPostal(csv_file):
    df = csv_file
    print(df.info())

Button(raiz, text="Abrir Archivo", command=leerCSV).pack()

# Mantener la aplicación gráfica abierta
raiz.mainloop() 

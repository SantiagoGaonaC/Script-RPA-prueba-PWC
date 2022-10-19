from __future__ import print_function
from tkinter import *
from tkinter import filedialog
import pandas as pd
import matplotlib as plt

raiz = Tk()

def abrirCSV():
    #askopenfilename permite desplegar la ventada que se abre el archivo
    #se pone solo una tupla como formato único CSV (filetypes=(("CSV Files","*.csv"),)
    #cambiar initialdir C:/
    csv_dir = filedialog.askopenfilename(title="abrir", initialdir="D:\PWC\Prueba 2", filetypes=(("CSV Files","*.csv"),))
    return csv_dir

#pandas lee el CSV y empieza la limpieza por metodos
def leerCSV():
    csv_file = pd.read_csv(abrirCSV())
    cambioNombreColumnas(csv_file)

#cambio de nombre columna Código Postal a Codigo_Postal (para que se pueda usar)
def cambioNombreColumnas(csv_file):
    csv_file = csv_file
    csv_file2 = csv_file.rename(columns={'Código postal':'Codigo_Postal'})
    limpiezaCodigoPostal(csv_file2)

# 2.a = Según políticas de la empresa ABC la columna “Código postal” solo debe tener números
def limpiezaCodigoPostal(csv_file2):
    csv_file2 = csv_file2
    # -------------- Expresiones regulares ^\d+$ ------------------------------
    # ^ anclar a la izquierda para que comience al principio de la cadena
    # \d digito cualquiera de 0 a 9
    # + detras de \d repetir una o más veces (por que es posible que se repita uno o más dígitos)
    # $ anclar a la derecha para que no pueda hacer otra cosa detrás de los digitos
    #------------------------------------------------------------------------------------
    csv_file3 = csv_file2.drop(csv_file2[csv_file2.Codigo_Postal.str.contains(r'[^\d+$]')].index) 
    # csv_file3 => se elimina todas las filas diferentes a la expresión regular y crear nuevo df # 3
    print(csv_file3)

# 3.a En una nueva columna "Notifica gerente" agregan el texto "Notificar" en caso de que el ...
# ... valor de la columna “Total” sea mayor a 80.8

Button(raiz, text="Abrir Archivo", command=leerCSV).pack()

# Mantener la aplicación gráfica abierta
raiz.mainloop() 

import multiprocessing
from tkinter import *
from tkinter import filedialog
from matplotlib.backend_bases import FigureCanvasBase
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
#import matplotlib as plt
import numpy as np
import re
import locale
import envio_gerente
import envio_encargado
import gen_graficas
from decouple import config
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#-----  USUARIO_G QUE ENVIA CORREO A GERENTE ---------
email_usuario_g = config('email_usuario_g')
contraseña_usuario_g = config('contraseña_usuario_g')
#----------------------------------------------------

#---- EMAIL DEL GERENTE | QUE RECIBE DEL usuario_g ----
email_gerente = config('email_gerente')
#----------------------------------------------------

#----- EMAIL DEL USUARIO_E QUIEN ENVIA AL ENCARGADO --------
email_usuario_e = config('email_usuario_e')
contraseña_usuario_e = config('contraseña_usuario_e')
#----------------------------------------------------

#----- EMAIL DEL ENCARGADO | CORREO TEMP -------------
email_encargado = config('email_encargado')
#-----------------------------------------------------

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
    limpiezaCorreo(csv_file3)

def limpiezaCorreo(csv_file3):
    df = csv_file3
    #si el correo no es valido cambiar y tiene prueba en NO cambiar la prueba a YES
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    df['Correo_Valido'] = df['Correo'].apply(lambda x: 'Yes' if pattern.match(x) else 'No')
    limpiezaFormatoDia(df)
    
def limpiezaFormatoDia(df):
    #establece el lenguaje ES y el tiempo local
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    df['Día'] = pd.to_datetime(df.Día)
    #config de la columna día
    df['Dia*'] = df['Día'].dt.strftime('%d/%m/%Y')
    validacionEnvio(df)
    
def validacionEnvio(df):
    df = df
    # cuando prueba sea NO & Notifica Encargado Yes & Correo Valido YES = Notificacion Correcta
    df['Notificaciones'] = np.where((df['Prueba']=='No')&(df['Notifica encargado']=='Yes')&(df['Correo_Valido']=='Yes'),'Yes','No')
    notificaGerente(df)

# 3.a En una nueva columna "Notifica gerente" agregan el texto "Notificar" en caso de que el ...
# ... valor de la columna “Total” sea mayor a 80.8
def notificaGerente(csv_file3):
    df = csv_file3
    df.Total = df.Total.str.replace('$','',regex=True)
    df['Total'] = df['Total'].astype('float64')
    df['Notifica_Gerente']=np.where((df['Total']>80.8)&(df['Notificaciones']=='Yes'),'Yes','No')
    csv_file4 = df
    dominioCorreo(csv_file4)
    
# 3.b En una nueva columna "Dominio" agregan el texto que se encuentra después del @ y ...
# ... antes del primer . (punto) del email encontrado en la columna “Correo”
def dominioCorreo(csv_file4):
    df = csv_file4
    df['Dominio'] = (df['Correo'].str.split('@').str[1]).str.rsplit('.').str[0]
    csv_file5 = df
    envioLocalInternacional(csv_file5)

#En una nueva columna "Envío" si la columna “Pais” corresponde a Estados Unidos, se ...
# ... indica que el envío es “Local”, de lo contrario es “Internacional”.
def envioLocalInternacional(csv_file5):
    df = csv_file5
    df['Envio']=np.where(df['País']=='United States','Local','Internacional')
    csv_file6 = df
    codigoRecepcion(csv_file6)

# En una nueva columna "Código recepción" agregan la concatenación de la columna ...
# ...“Código postal” con la columna “Token”.
def codigoRecepcion(csv_file6):
    df = csv_file6
    df['Codigo_recepcion'] = df.Codigo_Postal.str.cat(df.Token)
    df.to_csv('test.csv', header=True, index=False)
    gen_email_graficos(df)

#método para iniciar la creación de las graficas y enviar los correos
def gen_email_graficos(df):
    gen_graficas.gen_graficos(df)
    envios_email(df)

def envios_email(df):
    envio_gerente.envioEmailGerente(df,email_usuario_g,contraseña_usuario_g,email_gerente)
    envio_encargado.envio_email_encargado(df,email_usuario_e,contraseña_usuario_e,email_encargado)

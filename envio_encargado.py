""" 
Por cada fila de la tabla validan si deben notificar al encargado (Columna “Notificar encargado”) 
y realizan el envío de un correo al encargado con la información de las siguientes columnas 
“Nombre”, “Teléfono”, “Correo”, “Dirección”, “Marca”, “Envío”, “Código postal”, “Repuestos” y 
“Dominio”. Para la notificación al Encargado no existe un template estandarizado dado que cada 
usuario maneja su propia plantilla, sin embargo, el destinatario del correo siempre es la persona 
que les envió el archivo plano (.csv) del cual proviene toda la información. 
"""
#Para notifiar al encargado primero se debe comprobar si los datos de envio son validos!
from cgitb import html
from email.message import EmailMessage
import ssl
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import time #info-asunto-formato del mensaje etc...
from str_html import html_estructura
import time

def envio_email_encargado(df,email_usuario_e,contraseña_usuario_e,email_encargado):
    contador = 0
    # cantidad de yes = print(df['Notificaciones'].value_counts().to_frame())
    for i in df.loc[df['Notificaciones']=='Yes'].index:
        contador += 1 
        if contador != 70:
            test(df,email_usuario_e,contraseña_usuario_e,email_encargado,i,contador)
        elif contador == 70:
            time.sleep(90)
            contador == 0
            test(df,email_usuario_e,contraseña_usuario_e,email_encargado,i,contador)

def test(df,email_usuario_e,contraseña_usuario_e,email_encargado,i,contador):
    fecha_p = (df['Dia*'][i])
    fecha_s = df['Día'][i].strftime('%A')+", " + df['Día'][i].strftime('%d de %B de %Y')
    asunto = (f"""*Notificación sobre Pedido {df['Codigo_recepcion'][i]} {fecha_p}""")
        
    em = MIMEMultipart("alternative")
    em['From'] = email_usuario_e
    em['To'] = email_encargado
    em['Subject'] = asunto
        #em.set_content(cuerpo)
        
    html = html_estructura(df,i)
    parte_html = MIMEText(html, "html")
    em.attach(parte_html)
        
        #SSL seguridad = mantiene conexión segura ...
        # ... al enviar data entre dos sistemas
    contexto = ssl.create_default_context()
            # ------------  Enviar correo --------------
        # Define servidor, puerto y usar el contexto
        # para el envio se usa smtplib
        #se define el servidor, en este caso GMAIL
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls(context=contexto)
        smtp.login(email_usuario_e, contraseña_usuario_e)
            #as_string se da el formato correcto
        smtp.sendmail(email_usuario_e, email_encargado, em.as_string())
        print("Mensaje enviado encargado")
        
#extraer los datos en variable del dataframe =>
# => "Nombre”, “Teléfono”, “Código recepción”, “Total” y “Día”
# ejecución del codigo para el envio del email
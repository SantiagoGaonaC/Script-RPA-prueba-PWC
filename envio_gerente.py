from email.message import EmailMessage
import ssl
import smtplib
import datetime

def envioEmailGerente(df,email_usuario_g,contraseña_usuario_g,email_gerente):
    for i in df.loc[df['Notifica_Gerente']=='Yes'].index:
        fecha_p = (df['Dia*'][i])
        fecha_s = df['Día'][i].strftime('%A')+", " + df['Día'][i].strftime('%d de %B de %Y')
        
        asunto = "Notificación importante sobre Pedido "+df['Codigo_recepcion'][i]+" "+fecha_p
    
        cuerpo = (f"""Estimado Gerente,
Remito información sobre el pedido {df['Codigo_recepcion'][i]} que requiere una alta
atención por parte de la gerencia solicitado el día {fecha_s}

Nombre del cliente: {df['Nombre'][i]}
Teléfono del cliente: {df['Teléfono'][i]} 
Pedido: {df['Codigo_recepcion'][i]}
Total: ${str(df['Total'][i])}
Saludos.
""")
    
        em = EmailMessage()
        em['From'] = email_usuario_g
        em['To'] = email_gerente
        em['Subject'] = asunto
        em.set_content(cuerpo)
    
        #SSL seguridad = mantiene conexión segura ...
        # ... al enviar data entre dos sistemas

        contexto = ssl.create_default_context()
        
            # ------------  Enviar correo --------------
        # Define servidor, puerto y usar el contexto
        # para el envio se usa smtplib

        #se define el servidor, en este caso GMAIL
        
        
        
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls(context=contexto)
            smtp.login(email_usuario_g, contraseña_usuario_g)
            #as_string se da el formato correcto
            smtp.sendmail(email_usuario_g, email_gerente, em.as_string())
            print("Mensaje enviado gerente")
#extraer los datos en variable del dataframe =>
# => "Nombre”, “Teléfono”, “Código recepción”, “Total” y “Día”
# ejecución del codigo para el envio del email
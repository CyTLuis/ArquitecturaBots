# ===========================================================================
# Importaciones de clases y librerias necesarias
# ===========================================================================

# Region Llamado de clases o librerias necesarias
import smtplib 
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
# Endregion Llamado de clases o librerias necesarias


# ===========================================================================
# VARIABLES GLOBALES - LOCALES
# ===========================================================================
# Region Instancia de las clases y generación de var globales
msg = MIMEMultipart()

# En los destinatarios se separa el array por comas y se deja en lista
# '<Correo1@emergiacc.com>','<Correo2@emergiacc.com>'

# Endregion Instancia de las clases y generación de var globales

class Correo:
    """
        Correo
        ======
        Desde esta clase nos encargamos del envio de correos del bot
        estos correos pueden ser multiples o de reporte final, se debería
        modificar, según la necesidad del bot.
        ### `Usos`:
        - Podemos usar el servicio para reportar la finalización del bot.
    """
    def __init__(self):
        """
            Instancia de variables usadas dentro de la clase.
            - Se instancia el `remitente`, `destinatario(s)`, y `asunto del correo`.
        """
        self.__remitente = "<email@gmail.com>" 
        self.__asuntoCorreo= "Alerta Bot" 
        self.__destinatarios = ['<bot@gmail.com>']
         
    def EjecutarEnvioCorreo(self):
        """
            Este metodo se encargará de enviar un correo
            con la configuración dada en el constructor de la clase
            ### `Nota:`
            - Para enviar `formato HTML` desde python, se deberá definir el 
            cuerpo de mensaje como HTML, y generar una variable con el HTML 
            y dentro de cada etiqueta, el estilo que se le quiere dar.
            - Para enviar `archivos adjuntos` debemos abrir el archivo en 
            formato RB, y cerrar el mismo, y hacer un attach a la variable del correo.
        """
        mensajeCorreo = "¡Hola!\n Este es un correo enviado desde la automatización."
        msg.attach(MIMEText(mensajeCorreo, 'plain')) 

        msg['Subject'] = self.__asuntoCorreo
        smtp = smtplib.SMTP()
        smtp.starttls() 
        email = msg.as_string() 
        smtp.sendmail(self.__remitente, self.__destinatarios, email)
    
    


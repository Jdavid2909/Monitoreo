import psutil
import socket
import smtplib
from email.mime.text import MIMEText
import multiprocessing

def mostrar_informacion_cpu():
    print("Uso de la CPU:")
    print(" - Porcentaje total:", psutil.cpu_percent(), "%")
    print(" - Porcentaje por núcleo:", psutil.cpu_percent(percpu=True), "%")

def mostrar_informacion_memoria():
    print("Uso de la memoria:")
    print(" - Total:", psutil.virtual_memory().total)
    print(" - Disponible:", psutil.virtual_memory().available)
    print(" - Porcentaje de uso:", psutil.virtual_memory().percent, "%")

def mostrar_informacion_disco():
    print("Uso del disco:")
    print(" - Total:", psutil.disk_usage('/').total)
    print(" - Disponible:", psutil.disk_usage('/').free)
    print(" - Porcentaje de uso:", psutil.disk_usage('/').percent, "%")



# Ejemplo de uso
mostrar_informacion_cpu()
mostrar_informacion_memoria()
mostrar_informacion_disco()
num_procesadores = multiprocessing.cpu_count()
print("Número de procesadores:", num_procesadores)

direccion_ip = "192.168.0.100"
puerto = 1234

remitente = "tu-correo@gmail.com"
destinatario = "destinatario@gmail.com"
contraseña = "tu-contraseña"
asunto = "Uso de memoria excedido"

umbral_memoria = 40


uso_memoria = psutil.virtual_memory().percent
if uso_memoria > umbral_memoria:
 
    mensaje = MIMEText(f"El uso de memoria ha superado el umbral. Uso actual: {uso_memoria} %")
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto

    servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
    servidor_smtp.starttls()
    servidor_smtp.login(remitente, contraseña)
    servidor_smtp.sendmail(remitente, destinatario, mensaje.as_string())
    servidor_smtp.quit()

    print("Correo electrónico enviado correctamente.")
else:
    print("El uso de memoria está dentro del umbral.")

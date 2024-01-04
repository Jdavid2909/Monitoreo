import psutil
import smtplib
from email.mime.text import MIMEText
import multiprocessing

def mostrar_informacion_cpu():
    print("\nUso de la CPU:")
    print(" - Porcentaje total:", psutil.cpu_percent(), "%")
    print(" - Porcentaje por nucleo:", psutil.cpu_percent(percpu=True), "%")

def mostrar_informacion_memoria():
    print("\nUso de la memoria:")
    print(" - Total:", psutil.virtual_memory().total)
    print(" - Disponible:", psutil.virtual_memory().available)
    print(" - Porcentaje de uso:", psutil.virtual_memory().percent, "%")

def mostrar_informacion_disco():
    print("\nUso del disco:")
    print(" - Total:", psutil.disk_usage('/').total)
    print(" - Disponible:", psutil.disk_usage('/').free)
    print(" - Porcentaje de uso:", psutil.disk_usage('/').percent, "%")

def obtener_rendimiento(ip):
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    num_procesadores = multiprocessing.cpu_count()

    print(f"\nUso de CPU en {ip}: {cpu_percent}%")
    print(f"\nUso de memoria en {ip}: {memory_percent}%")
    print(f"\nUso de disco en {ip}: {disk_percent}%")
    print(f"\nNumero de procesadores en {ip}: {num_procesadores}%")

# Ejemplo de uso
mostrar_informacion_cpu()
mostrar_informacion_memoria()
mostrar_informacion_disco()
num_procesadores = multiprocessing.cpu_count()
print("\nNumero de procesadores:", num_procesadores)

ip = "192.168.0.103"
print("\n================================================================")
obtener_rendimiento(ip)
print("\n================================================================")

remitente = "jonatan14yanacallo@gmail.com"
destinatario = "yanacallojonatan@gmail.com"
contraseña = "munoz2001uce"
asunto = "Uso de memoria excedido"

umbral_memoria = 40


uso_memoria = psutil.virtual_memory().percent
if uso_memoria > umbral_memoria:
    mensaje = MIMEText(f"\nEl uso de memoria ha superado el umbral. Uso actual: {uso_memoria} %")
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto

    servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
    servidor_smtp.starttls()
    servidor_smtp.login(remitente, contraseña)
    servidor_smtp.sendmail(remitente, destinatario, mensaje.as_string())
    servidor_smtp.quit()

    print("\nCorreo electrónico enviado correctamente")
else:
    print("\nEl uso de memoria está dentro del umbral")

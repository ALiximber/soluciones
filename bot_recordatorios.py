from plyer import notification
import time

recordatorios = [
    ("Tomar agua", 10),
    ("Estirarse", 30)
]

for mensaje, minutos in recordatorios:
    time.sleep(minutos * 60)
    notification.notify(title="Recordatorio", message=mensaje, timeout=10)

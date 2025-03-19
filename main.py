import time
from api_meteo import get_weather
import socket
esp_ip = "192.168.4.1"
port = 2025
end = "not"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((esp_ip, port))
print(f"Connecté à l'ESP32 ({esp_ip}:{port})")
message = "Hello ESP32!\n"  # On ajoute '\n' car l'ESP attend une fin de ligne
sock.sendall(message.encode())  # Envoie en binaire

print(f"Message envoyé: {message}")

# Fermeture de la connexion
sock.close()

def check_meteo():
    get_weather

while end == "not" :
    check_meteo
    time.sleep(5)

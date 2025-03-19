import time
from api_meteo import get_weather
import socket
from dotenv import load_dotenv
import os

# Load values from .env file
load_dotenv()
ESP_IP = os.getenv("ESP_IP")
PORT = int(os.getenv("ESP_PORT"))

# Set default values
end = "not"

# First connection to ESP32
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ESP_IP, PORT))
print(f"[{'\033[32m'}OK{'\033[0m'}] - connection configuration")
message = "ping\n"  # On ajoute '\n' car l'ESP attend une fin de ligne
sock.sendall(message.encode())  # Envoie en binaire

response = sock.recv(1024).decode().strip()
if response == "ping":
    print(f"[{'\033[32m'}OK{'\033[0m'}] - connection to esp")
    sock.close()

# Main
while end == "not" :
    get_weather
    time.sleep(5)

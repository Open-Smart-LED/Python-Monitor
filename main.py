import time
from api_meteo import get_weather
import socket
from dotenv import load_dotenv
import os
from algo_adaptation import algo_adaptation

# Load values from .env file
load_dotenv()
ESP_IP = os.getenv("ESP_IP")
PORT = int(os.getenv("ESP_PORT"))
NB_LED = int(os.getenv("NB_LED"))

# Set default values
end = "not"

# Setup connection to ESP32
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ESP_IP, PORT))
print(f"[{'\033[32m'}OK{'\033[0m'}] - connection established")

response = sock.recv(1024).decode().strip()
if response == "setup":
    message = f"{NB_LED}\n" # On ajoute '\n' car l'ESP attend une fin de ligne
    sock.sendall(message.encode())  # Envoie en binaire
    print(f"[{'\033[32m'}OK{'\033[0m'}] - setup send")
    sock.close()

# Main
while end == "not" :
    description, cloud, temperature, sunrise, sunset = get_weather()
    result = algo_adaptation(description, cloud, temperature, sunrise, sunset)
    sock.connect((ESP_IP, PORT))
    sock.sendall(result.encode())  # Envoie en binaire
    print(f"[{'\033[32m'}OK{'\033[0m'}] - result sent")
    sock.close()
    time.sleep(10)

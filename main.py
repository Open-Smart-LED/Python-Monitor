import time
import socket
from dotenv import load_dotenv
import os
from api_meteo import get_weather
from algo_adaptation import algo_adaptation

##### Load values from .env file #####
load_dotenv()
ESP_IP = os.getenv("ESP_IP")
PORT = int(os.getenv("ESP_PORT"))
NB_LED = int(os.getenv("NB_LED"))
CONFIG_STATE = os.getenv("CONFIG_STATE")

##### Verifie .env configuration #####
if CONFIG_STATE != "Finish":
    print(f"[{'\033[31m'}FAIL{'\033[0m'}] - File .env is not configure")
    exit()

##### Setup ESP32 #####
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ESP_IP, PORT))
print(f"[{'\033[32m'}OK{'\033[0m'}] - connection established")

response = sock.recv(1024).decode().strip()
if response == "setup":
    message = f"{NB_LED}\n" # On ajoute '\n' car l'ESP attend une fin de ligne
    sock.sendall(message.encode())
    print(f"[{'\033[32m'}OK{'\033[0m'}] - setup send")
    sock.close()

##### Main #####
while True :
    meteo = get_weather()
    if meteo is not None:
        description, cloud, temperature, sunrise, sunset = meteo
        result = algo_adaptation(description, cloud, temperature, sunrise, sunset)
        print(f"[{'\033[34m'}INFO{'\033[0m'}] - color result : ", result)
        if sock:
            sock.close()  # Fermer proprement l'ancien socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ESP_IP, PORT))
        sock.sendall(result.encode())
        print(f"[{'\033[32m'}OK{'\033[0m'}] - result sent")
        sock.close()

    time.sleep(10) # En seconde
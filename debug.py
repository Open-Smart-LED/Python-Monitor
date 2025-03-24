import socket
import os
from dotenv import load_dotenv

load_dotenv()
ESP_IP = os.getenv("ESP_IP")
PORT = int(os.getenv("ESP_PORT"))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ESP_IP, PORT))

msg = input("msg : ")
sock.sendall(msg.encode())

while True :
    r = input("r : ")
    g = input("g : ")
    b = input("b : ")
    msg = f"{r},{g},{b}\n"
    sock.sendall(msg.encode())
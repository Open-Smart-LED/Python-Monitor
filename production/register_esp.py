import serial
import time
import os
import argparse
import jwt as pyjwt
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path

parser = argparse.ArgumentParser(description="Script for register new esp in OpenSmartLED database")
parser.add_argument("-p", "--port", required=True, help="Port série (ex: COM7)")
args = parser.parse_args()

chipID = ""

# Database path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
database_path = os.path.join(PARENT_DIR, "database.json")


def create_jwt(esp_id):
    SECRET = "Your Password"

    payload = {
        "id": esp_id,
        "exp": datetime.now(timezone.utc) + timedelta(days=1)
    }

    token = pyjwt.encode(payload, SECRET, algorithm="HS256")
    TokenJWT = token
    add_esp(esp_id, token)
    return(token)

def add_esp(id, jwt):
    data = load_data()
    data["esps"].append({"id": id, "jwt": jwt})
    save_data(data)

def load_data():
    database_path2 = Path(database_path)
    if not database_path2.exists():
        return {"esps": []}
    with open(database_path, "r") as f:
        return json.load(f)
    
def save_data(data):
    with open(database_path, "w") as f:
        json.dump(data, f, indent=4)



# Ouvre le port série
ser = serial.Serial(args.port, 115200, timeout=2)  # Remplace COM5 par ton port
time.sleep(8)  # Attendre que l'ESP redémarre et envoie les infos

while True:
    chipID = ser.readline().decode('utf-8').strip()
    if chipID != "":
        print(chipID)
        break

ser.close()

TokenJWT = create_jwt(chipID)

with open("debug/values.h", "a") as f:
    f.write(f'#ifndef SECRETS_H\n#define SECRETS_H\n\nconst char* jwtToken = "{TokenJWT}";\n\n#endif')

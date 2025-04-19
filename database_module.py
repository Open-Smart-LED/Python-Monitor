import json
from pathlib import Path
import os

DATA_FILE = Path("database.json")

# Charger les données JSON
def load_data():
    chemin_relatif = "~/Python-Monitor/database.json"
    chemin_absolu = os.path.expanduser(chemin_relatif)
    DATA_FILE = Path(chemin_absolu)
    if not DATA_FILE.exists():
        return {"esps": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Enregistrer les données JSON
def save_data(data):
    chemin_relatif = "~/Python-Monitor/database.json"
    chemin_absolu = os.path.expanduser(chemin_relatif)
    DATA_FILE = Path(chemin_absolu)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Ajouter un nouvel ESP
def add_esp(id, jwt):
    data = load_data()
    data["esps"].append({"id": id, "jwt": jwt})
    save_data(data)

# Lire tous les ESP
def get_esps():
    data = load_data()
    return data["esps"]

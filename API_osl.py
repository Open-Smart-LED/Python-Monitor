from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

########## Load values from .env file ##########
load_dotenv()
NB_LED = int(os.getenv("NB_LED"))
CONFIG_STATE = os.getenv("CONFIG_STATE")


########## Verifie .env configuration ##########
if CONFIG_STATE != "Finish":
    print(f"[{'\033[31m'}FAIL{'\033[0m'}] - File .env is not configure")
    exit()


########## Define API ###########
app = FastAPI()

class Item(BaseModel): # Modèle de données
    name: str
    price: float
    in_stock: bool = True


########## API Routes ###########
@app.get("/")
def read_root():
    return {"message": "Bienvenue dans ton API 🚀"}

@app.get("/version/")
def get_version():
    return {"Version": "0.1"}

@app.get("/led/")
def get_led():
    return {"LEDs": NB_LED}

@app.post("/items/")
def create_item(item: Item):
    return {"message": f"Objet '{item.name}' enregistré avec succès.", "data": item}

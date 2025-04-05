from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from api_meteo import get_weather
from algo_adaptation import algo_adaptation

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

class ESP(BaseModel): # Modèle de données
    name: str
    ip: str
    user: str


########## API Routes ###########
@app.get("/")
def read_root():
    return {"message": "Welcome on OpenSmartLED !"}

@app.get("/version/")
def get_version():
    return {"Version": "0.1"}

@app.get("/led/")
def get_led():
    return {"LEDs": NB_LED}

@app.get("/test/")
def get_test():
    main()
    return {"TEST": "fait"}

@app.post("/addesp/")
def create_esp(item: ESP):
    return {"check": "ok"}

'''@app.post("/items/")
def create_item(item: Item):
    return {"message": f"Objet '{item.name}' enregistré avec succès.", "data": item}'''

def main():
    meteo = get_weather()
    if meteo is not None:
        cloud, temperature, sunrise, sunset = meteo
        result = algo_adaptation(cloud, temperature, sunrise, sunset)
        print(f"[{'\033[34m'}INFO{'\033[0m'}] - color result : ", result)
        print(f"[{'\033[32m'}OK{'\033[0m'}] - result sent")
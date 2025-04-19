from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from api_meteo import get_weather
from algo_adaptation import algo_adaptation
from database_module import get_esps, add_esp
from jwt_module import verify_token
from fastapi import Depends

########## Load values from .env file ##########
load_dotenv()
NB_LED = int(os.getenv("NB_LED"))
GPIO_LED = int(os.getenv("GPIO_LED"))
CONFIG_STATE = os.getenv("CONFIG_STATE")


########## Verifie .env configuration ##########
if CONFIG_STATE != "Finish":
    print(f"[{'\033[31m'}FAIL{'\033[0m'}] - File .env is not configure")
    exit()

########## Define API ###########
app = FastAPI()

class ESP(BaseModel):
    name: str
    owner: str
    id: str

########## API Routes ###########
@app.get("/")
def read_root():
    return {"message": "Welcome on OpenSmartLED !"}

@app.get("/version/")
def get_version():
    return {"Version": "0.1"}

@app.get("/config/")
def get_config(token_verif=Depends(verify_token)):
    return {"LEDs": NB_LED, "GPIO": GPIO_LED}

@app.get("/rgb/")
def get_rgb(token_verif=Depends(verify_token)):
    r, g, b = main()
    return {"red": r, "green": g, "blue": b}

@app.get("/esps/")
def list_esps(token_verif=Depends(verify_token)):
    return get_esps()

@app.post("/esps/")
def create_esp(esp: ESP, token_verif=Depends(verify_token)):
    add_esp(esp.name, esp.owner, esp.id)
    return {"message": "ESP ajouté"}


def main():
    meteo = get_weather()
    if meteo is not None:
        cloud, temperature, sunrise, sunset = meteo
        r, g, b = algo_adaptation(cloud, temperature, sunrise, sunset)
        print(f"[{'\033[34m'}INFO{'\033[0m'}] - color result : ", r, g, b)
        print(f"[{'\033[32m'}OK{'\033[0m'}] - result sent")
        return(r, g, b)
    return (100, 0, 0)
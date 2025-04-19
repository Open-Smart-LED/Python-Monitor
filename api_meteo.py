import requests
from datetime import datetime
from dotenv import load_dotenv
import os

def meteo_setup():
    load_dotenv()
    API_KEY = os.getenv("API_METEO")
    VILLE = os.getenv("LOCATION")
    UNITS = os.getenv("UNITS")
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={VILLE}&appid={API_KEY}&units={UNITS}&lang=en"
    return (URL)

def get_weather():
    URL = meteo_setup()
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        data = response.json()
        
        temperature = data["main"]["temp"]
        #description = data["weather"][0]["description"] Utile ?
        sunrise =  data["sys"]["sunrise"]
        sunset = data["sys"]["sunset"]
        cloud = data["clouds"]["all"]

        print(f"[{'\033[32m'}OK{'\033[0m'}] - meteo check")
        print(f"[{'\033[34m'}INFO{'\033[0m'}] - ", cloud,",", temperature,",", sunrise,",", sunset)
        return(cloud, temperature, sunrise, sunset)

    except requests.exceptions.RequestException as e:
        print(f"[{'\033[31m'}FAIL{'\033[0m'}] - meteo check : ", e)
        return(None)
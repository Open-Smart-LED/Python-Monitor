import time
from api_meteo import get_weather
end = "not"

def check_meteo():
    get_weather

while end == "not" :
    check_meteo
    time.sleep(5)

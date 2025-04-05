import time
import socket
from api_meteo import get_weather
from algo_adaptation import algo_adaptation

while True :
    meteo = get_weather()
    if meteo is not None:
        cloud, temperature, sunrise, sunset = meteo
        result = algo_adaptation(cloud, temperature, sunrise, sunset)
        print(f"[{'\033[34m'}INFO{'\033[0m'}] - color result : ", result)
        print(f"[{'\033[32m'}OK{'\033[0m'}] - result sent")

    time.sleep(10) # En seconde
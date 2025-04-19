from datetime import datetime, timedelta

def algo_adaptation(cloud, temperature, sunrise, sunset):
    print(f"[{'\033[32m'}OK{'\033[0m'}] - algo start")

    realtime = datetime.now()
    sunrise = datetime.fromtimestamp(sunrise)
    sunset = datetime.fromtimestamp(sunset)
    marge = timedelta(minutes=3)
    
    if sunrise - marge <= realtime <= sunrise + marge:
        print(f"[{'\033[34m'}INFO{'\033[0m'}] - sunrise detect")
        return (0,0,0)
    elif sunset - marge <= realtime <= sunset + marge:
        print(f"[{'\033[34m'}INFO{'\033[0m'}] - sunset detect")
        return (255,255,255)
    

    return (255,255,255)
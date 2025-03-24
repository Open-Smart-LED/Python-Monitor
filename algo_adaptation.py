def algo_adaptation(description, cloud, temperature, sunrise, sunset):
    print("algo sart")
    if description == "clear sky":
        description = 100
        final_lum = (description + cloud) / 2
        return ("255,255,255")
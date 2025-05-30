def check_weather(temperature: float) -> str:
    if temperature > 20:
        return "hot"
    elif 10 < temperature <= 20:
        return "average"
    else:
        return "cold"
    
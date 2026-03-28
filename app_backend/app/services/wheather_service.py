import os
import requests

OPENWHEATHERMAP_API_KEY=os.getenv("OPENWHEATHERMAP_API_KEY")

def fetch_wheather(lat: float, lon:float):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPENWHEATHERMAP_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return {
        "temperature": data["main"]["temp"],
        "wind_speed": data["wind"]["speed"],
        "wind_direction": data["wind"]["deg"],
        "description": data["weather"][0]["description"]
    }

if __name__ == "__main__":
    print("A testar API do clima...")

    result = fetch_wheather(41.1579, -8.6291)

    print("Resultado:")
    print(result)
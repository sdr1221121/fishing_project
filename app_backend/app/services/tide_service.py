import requests
import datetime
import os

STORMGLASS_API_KEY = os.getenv("STORMGLASS_API_KEY")


def fetch_tide(lat: float, lon:float):
    now = datetime.datetime.utcnow()

    start = int(now.replace(hour=0, minute=0, second=0).timestamp())
    end = int(now.replace(hour=23, minute=59, second=59).timestamp())

    response = requests.get(
        'https://api.stormglass.io/v2/tide/extremes/point',
        params={
            'lat': lat,   
            'lng': lon,
            'start': start,
            'end': end,
        },
        headers={
            'Authorization': STORMGLASS_API_KEY
        }
    )

    if response.status_code != 200:
        print("Erro:", response.status_code)
        print(response.text)
        return None

    data = response.json()

    return data


# 🔥 TESTE DIRETO
if __name__ == "__main__":
    print("A testar API de marés...")

    result = fetch_tide()

    print("Resultado:")
    print(result)
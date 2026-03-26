import requests
import datetime

key_stormglass = ""


def fetch_tide():
    now = datetime.datetime.utcnow()

    start = int(now.replace(hour=0, minute=0, second=0).timestamp())
    end = int(now.replace(hour=23, minute=59, second=59).timestamp())

    response = requests.get(
        'https://api.stormglass.io/v2/tide/extremes/point',
        params={
            'lat': 41.1579,   # Porto
            'lng': -8.6291,
            'start': start,
            'end': end,
        },
        headers={
            'Authorization': key_stormglass
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
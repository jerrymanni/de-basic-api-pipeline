import time
from datetime import datetime, timezone


def transform(data):

    try:
        coords = data["coord"]
        lon = coords["lon"]
        lat = coords["lat"]

        temp = data["main"]["temp"]

        timestamp = datetime.fromtimestamp(data["dt"], tz=timezone.utc)
    except Exception as e:
        print(f"Ei onnistunut tietojen haku! Virhe: {e}")
        raise

    print(f"Longitude = {lon}, latitude = {lat}, temperature = {temp}, timestamp = {timestamp}")

    return {
        "lon": lon,
        "lat": lat,
        "temp": temp,
        "timestamp": timestamp
    }
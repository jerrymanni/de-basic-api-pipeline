from typing import Any
from datetime import datetime, timezone


def transform(data: dict[str, Any]) -> dict[str, Any]:

    try:
        coords: dict = data["coord"]
        lon: float = coords.get("lon", 99.99)
        lat: float = coords.get("lat", 99.99)

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
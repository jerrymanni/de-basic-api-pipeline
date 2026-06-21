from typing import Any
from datetime import datetime, timezone
from ..schemas.api import WeatherResponse


def transform(data: WeatherResponse) -> dict[str, Any]:

    try:
        coords = data.coord
        lon = coords.lon
        lat = coords.lat

        temp = data.main.temp

        timestamp = datetime.fromtimestamp(data.dt, tz=timezone.utc)
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
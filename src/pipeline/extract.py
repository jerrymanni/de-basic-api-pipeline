from typing import Any
import requests
from ..config.config import Settings
from ..schemas.api import WeatherResponse

settings = Settings()
COORDS = [("44.34", "10.99"), ("30.15", "20.13")]
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def extract_from_api(lat: str, long: str) -> WeatherResponse:

    url = f"{WEATHER_URL}?lat={lat}&lon={long}&units=metric&appid={settings.api_key}"
    try:
        request = requests.get(url)
        request.raise_for_status()

        response = WeatherResponse.model_validate(request.json())
    except Exception as e:
        print(f"Ei onnistunut haku! Virhe: {e}")

    return response


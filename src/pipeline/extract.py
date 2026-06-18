import requests
from ..config.config import Settings  # ty:ignore[unresolved-import]

settings = Settings()
COORDS = [("44.34", "10.99"), ("30.15", "20.13")]


def extract_from_api(lat: str, long: str) -> dict:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    #lat = "44.34"
    #long = "10.99"

    url = f"{BASE_URL}?lat={lat}&lon={long}&appid={settings.api_key}"

    request = requests.get(url)

    response = request.json()

    return response
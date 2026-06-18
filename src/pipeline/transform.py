import time
from datetime import datetime, timezone


def transform(data):

    coords = data["coord"]
    lon = coords["lon"]
    lat = coords["lat"]

    temp = data["main"]["temp"]

    timestamp = datetime.fromtimestamp(data["dt"], tz=timezone.utc)


    print(f"Longitude = {lon}, latitude = {lat}, temperature = {temp}, timestamp = {timestamp}")
from .extract import extract_from_api, COORDS
from .transform import transform

for lat, lon in COORDS:
    transform(
        extract_from_api(lat, lon)
    )
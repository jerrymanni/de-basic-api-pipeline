from .extract import extract_from_api, COORDS
from .transform import transform
from .load import load_to_db

for lat, lon in COORDS:
    load_to_db(
        transform(
            extract_from_api(lat, lon)
        )
    )
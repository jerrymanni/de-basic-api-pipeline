from typing import Any
import psycopg
from ..config.config import Settings

settings = Settings()
postgres_url = f"postgresql://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}/{settings.postgres_db}"

def load_to_db(data: dict[str, Any]) -> None:
    with psycopg.connect(postgres_url) as conn:

        with conn.cursor() as cur:
            print("Insert data into database")
            cur.execute(
                """
                insert into weather_data (
                location,
                lat,
                lon,
                temp,
                measurement_ts
                )
                values
                (%s, %s, %s, %s, %s)
                """,
                ("", data["lat"], data["lon"], data["temp"], data["timestamp"])
            )

            conn.commit()



from pydantic import BaseModel

class Coord(BaseModel):
    lon: float
    lat: float

class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str

class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int

class Wind(BaseModel):
    speed: float
    deg: int
    gust: float

class Clouds(BaseModel):
    all: int

class Sys(BaseModel):
    country: str
    sunrise: int
    sunset: int

class WeatherResponse(BaseModel):
    coord: Coord
    weather: list[Weather]
    base: str
    main: Main
    visibility: int
    wind: Wind
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int
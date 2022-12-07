from typing import Literal, TypeAlias
from urllib.request import urlopen
from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
import json
from coordinate import Coordinates
import config
Tem_Celsius: TypeAlias = float


class Wind_Direction(IntEnum):
    North = 0
    Northeast = 45
    East = 90
    Southeast = 135
    South = 180
    Southwest = 225
    West = 270
    Northwest = 315


@dataclass(slots=True, frozen=True)
class Weather:
    location: str
    temperature: Tem_Celsius
    temperature_feeling: Tem_Celsius
    description: str
    wind_speed: float
    wind_direction: Wind_Direction
    sunrise: datetime
    sunset: datetime

def wind_direction(openweather_dict: dict):
    degrees = openweather_dict['wind']['deg']
    degrees = round(degrees / 45) * 45
    degrees = 0 if degrees == 360 else degrees
    return Wind_Direction(degrees).name


def get_weather(coordinates=Coordinates):
    openweather_response = weather_response(
        longitude=coordinates.longitude, latitude=coordinates.latitude
    )
    weather = weather_repose(openweather_response)
    return weather


def weather_response(latitude: float, longitude: float):
    url = config.CURRENT_WEATHER_API_CALL.format(latitude=latitude, longitude=longitude)
    return urlopen(url).read()


def weather_repose(openweather_response: str):
    weather_dict = json.loads(openweather_response)
    return Weather(
        location=location(weather_dict),
        temperature=temperature(weather_dict),
        temperature_feeling=temperature_feeling(weather_dict),
        description=description(weather_dict),
        wind_speed=wind_speed(weather_dict),
        sunrise=sun_time(weather_dict, 'sunrise'),
        sunset=sun_time(weather_dict, 'sunset'),
        wind_direction=wind_direction(weather_dict)
    )


def location(weather_dict: dict):
    return weather_dict['name']


def temperature(weather_dict: dict):
    return weather_dict['main']['temp']


def temperature_feeling(weather_dict: dict):
    return weather_dict['main']['feels_like']


def description(weather_dict):
    return str(weather_dict['weather'][0]['description']).capitalize()


def sun_time(weather_dict: dict, time: Literal["sunrise", "sunset"]):
    return datetime.fromtimestamp(weather_dict['sys'][time])


def wind_speed(weather_dict: dict):
    return weather_dict['wind']['speed']


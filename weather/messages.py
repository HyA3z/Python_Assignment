from coordinate import get_coordinates
from api import get_weather
import emoji


def weather():
    wet = get_weather(get_coordinates())
    return f'{wet.location}, {wet.description}\n' \
           f'Temperature: {emoji.emojize(":thermometer:")} {wet.temperature}°C, \nApparent temperature: {emoji.emojize(":face_with_thermometer:")} {wet.temperature_feeling}°C'


def wind():
    wet = get_weather(get_coordinates())
    return f'{wet.wind_direction} wind and speed is : {emoji.emojize(":tornado:")} {wet.wind_speed} m/s'


def sun_time():
    wet = get_weather(get_coordinates())
    return f'Sunrise: {emoji.emojize(":sunrise:")} {wet.sunrise.strftime("%H:%M")}\n' \
           f'Sunset: {emoji.emojize(" :sunset:")} {wet.sunset.strftime("%H:%M")}\n'

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

Weather = InlineKeyboardButton('Weather', callback_data='weather')
Wind = InlineKeyboardButton('Wind speed', callback_data='wind')
Sun_time = InlineKeyboardButton('Sunrise Sunset Time', callback_data='sun_time')

WEATHER = InlineKeyboardMarkup().add(Wind, Sun_time)
WIND = InlineKeyboardMarkup().add(Weather).add(Sun_time)
SUN_TIME = InlineKeyboardMarkup().add(Weather, Wind)
HELP = InlineKeyboardMarkup().add(Weather, Wind).add(Sun_time)

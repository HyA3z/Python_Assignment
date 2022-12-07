BOT_API = '5825667491:AAHC1McDK8XB5Hi2hDUt8OW4rGr0G-qLMJ0'
WEATHER_API = '11d8ffeefbda76b226e10349504d2918'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API + '&units=metric'
)

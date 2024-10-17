import requests
import os
import json

def get_weather(city):
    with open('apikeys.json') as f:
        data = json.load(f)
        api = data['openweatherAPI_key']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
    response = requests.get(url)
    data = response.json()
    parsed_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }
    return parsed_data


get_weather('London')
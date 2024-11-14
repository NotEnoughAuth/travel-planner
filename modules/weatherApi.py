import requests
import os
import json

# Function to get the current weather based on City
def get_weather(city):
    # Load the API key
    with open('/app/apikeys.json') as f:
        data = json.load(f)
        api = data['openweatherAPI_key']

    # Send a request to the OpenWeatherMap API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=imperial'
    response = requests.get(url)
    data = response.json()

    # Parse the data for wanted information
    parsed_data = {
        'city': city,
        'weather': data['weather'][0]['main'],
        'temperature': data['main']['temp'],
        #'description': data['weather'][0]['description'],
    }

    # Format the wanted information to human readable format
    result = f"Current weather in {parsed_data['city']} is {parsed_data['weather'].lower()} with a temperature of {int(parsed_data['temperature'])}°F."

    return result
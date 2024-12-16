import os
import requests

def get_weather(location):
    """Fetch real-time weather data for a given location."""
    API_KEY = os.getenv('OPENWEATHER_API_KEY')
    if not API_KEY:
        raise ValueError("OPENWEATHER_API_KEY environment variable not set")

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    print(f"Running weather function for {location}...")
    
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"  # Celsius 
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code == 200:
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        city_name = data['name']
        return f"The weather in {city_name} is {temperature}°C with {weather_description}."
    else:
        return f"Could not get the weather for {location}. Please try again."
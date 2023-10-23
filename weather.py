import os
import requests
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

def get_current_weather(city="Patra"):
    request_url=f'https://api.weatherapi.com/v1/current.json?key={os.getenv("API_KEY")}&q={city}'
    weather_data=requests.get(request_url).json()
    
    return weather_data
    
    #pprint(weather_data)
    #print(f'\nCurrent weather for {weather_data["location"]["name"]}')
    #print(f'\nThe temp is {weather_data["current"]["temp_c"]} degrees Celsius')
    #print(f'\nFeels like {weather_data["current"]["feelslike_c"]} and {weather_data["current"]["condition"]["text"]}.')

if __name__=="__main__":
    print('\n*** Get Current Weather Conditions ***\n')
    city=input('\nPlease enter a city name:\n')
    if not bool(city.strip()):    #check if city is an empty string
        city="Paris"
    weather_data=get_current_weather(city)
    
    print("\n")
    pprint(weather_data)
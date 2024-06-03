from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Lyon"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&format=json&units=metric'

    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == '__main__':
    print('*** Get Weather Conditions ***')
    city = input("Enter the city name: ")

    if not bool(city.strip()):
        city = "Paris"

    weather_data = get_current_weather(city=city)
    pprint(weather_data)

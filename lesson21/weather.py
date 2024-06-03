import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


def get_current_weather():
    print('*** Current weather ***')

    latitude = "45.7485"
    longitude = "4.8467"
    request_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={
        longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&apikey={os.getenv('API_KEY')}"

    weather_data = requests.get(request_url).json()
    # pprint(weather_data)

    print(f"Current temperature: {
          weather_data['current']['temperature_2m']:.1f}°C")


if __name__ == '__main__':
    get_current_weather()

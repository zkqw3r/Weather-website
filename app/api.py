import aiohttp
import json
import asyncio
import os
from dotenv import load_dotenv
from app.converter import wind_direction, pick_icon, pressure_mmhg


load_dotenv()
API = os.getenv('API')
URL_CURRENT_WEATHER_FORECAST = 'https://api.openweathermap.org/data/2.5/weather'
URL_FIVE_DAY_WEATHER_FORECAST = 'https://api.openweathermap.org/data/2.5/forecast'


async def current_weather_data(city_name):
    """
    Function for getting information about the current weather in a certain city
    """

    async with aiohttp.ClientSession() as session:
        params = {
            'q':city_name,
            'units':'metric',
            'appid':API,
            'lang':'ru',
        }
        async with session.get(URL_CURRENT_WEATHER_FORECAST, params=params) as response:
            if response.status == 200:
                data = await response.json()
                if data.get("cod") == 200:
                    weather_Data = {
                        "status_code":data.get("cod"),
                        "name":data.get("name"),
                        "icon":await pick_icon(data.get("weather")[0].get("id")),
                        "weather":data.get("weather")[0].get("description"),
                        "temp":data.get("main").get("temp"),
                        "feels_like_temp":data.get("main").get("feels_like"),
                        "pressure":await pressure_mmhg(data.get("main").get("pressure")),
                        "wind_speed":data.get("wind").get("speed"),
                        "wind_direction":await wind_direction(data.get("wind").get("deg")),
                        }
                return weather_Data
            else:
                return None


if __name__=='__main__':
    print(asyncio.run(current_weather_data(city_name=input('city: '))))

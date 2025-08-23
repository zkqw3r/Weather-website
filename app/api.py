import aiohttp
import asyncio
import os
from dotenv import load_dotenv
from app.converter import wind_direction, pick_icon, pressure_mmhg, format_date
from datetime import datetime, timedelta
from collections import Counter


load_dotenv()
API = os.getenv('API')
URL_CURRENT_WEATHER_FORECAST = 'https://api.openweathermap.org/data/2.5/weather'
URL_FIVE_DAY_WEATHER_FORECAST = 'https://api.openweathermap.org/data/2.5/forecast'


async def get_current_weather_data(city_name):

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
                if str(data.get("cod")) == "200":
                    weather_data = {
                        "status_code":data.get("cod"),
                        "name":data.get("name"),
                        "icon":await pick_icon(data.get("weather")[0].get("id")),
                        "weather":data.get("weather")[0].get("description"),
                        "temp":f'+{int(round(data.get("main").get("temp")))} °C' if int(round(data.get("main").get("temp")))>0 else f'{int(round(data.get("main").get("temp")))} °C',
                        "feels_like_temp":f'+{int(round(data.get("main").get("feels_like")))} °C' if int(round(data.get("main").get("feels_like")))>0 else f'{int(round(data.get("main"))).get("feels_like")} °C',
                        "pressure":await pressure_mmhg(data.get("main").get("pressure")),
                        "wind_speed":int(round(data.get("wind").get("speed"))),
                        "wind_direction":await wind_direction(data.get("wind").get("deg")),
                        }
                    return weather_data
                return None
            return None
        

async def get_five_day_forecast_data(city_name):

    """
    Function for getting weather data with average values for time periods
    """

    async with aiohttp.ClientSession() as session:
        params = {
            'q': city_name,
            'units': 'metric',
            'appid': API,
            'lang': 'ru',
        }

        try:
            async with session.get(URL_FIVE_DAY_WEATHER_FORECAST, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    if str(data.get("cod")) == "200":
                        weather_data = {}
                        
                        all_forecasts = []
                        for forecast in data.get("list"):
                            dt_txt = forecast.get("dt_txt")
                            date_part = dt_txt[:10]
                            time_part = dt_txt[11:16]
                            hour = int(time_part.split(':')[0])
                            
                            forecast_data = {
                                "date": date_part,
                                "time": time_part,
                                "hour": hour,
                                "temp": forecast.get("main").get("temp"),
                                "temp_feels_like": forecast.get("main").get("feels_like"),
                                "pressure": forecast.get("main").get("pressure"),
                                "icon": await pick_icon(forecast.get("weather")[0].get("id")),
                                "weather": forecast.get("weather")[0].get("description"),
                                "wind_speed": forecast.get("wind").get("speed"),
                                "wind_direction": forecast.get("wind").get("deg"),
                            }
                            all_forecasts.append(forecast_data)

                        for forecast in all_forecasts:
                            target_date = forecast["date"]
                            hour = forecast["hour"]
                        
                            if hour <= 3:
                                try:
                                    current_date = datetime.strptime(target_date, "%Y-%m-%d")
                                    previous_date = current_date - timedelta(days=1)
                                    previous_date_str = previous_date.strftime("%Y-%m-%d")
                                    if previous_date_str in [f["date"] for f in all_forecasts]:
                                        target_date = previous_date_str
                                except:
                                    pass
                            
                            if target_date not in weather_data:
                                weather_data[target_date] = {
                                    "morning": {"forecasts": []},   # 6:00 - 9:00
                                    "day": {"forecasts": []},       # 12:00 - 15:00
                                    "evening": {"forecasts": []},   # 18:00 - 21:00
                                    "night": {"forecasts": []}      # 0:00 - 3:00
                                }
                    
                            if 6 <= hour <= 9:
                                weather_data[target_date]["morning"]["forecasts"].append(forecast)
                            elif 12 <= hour <= 15:
                                weather_data[target_date]["day"]["forecasts"].append(forecast)
                            elif 18 <= hour <= 21:
                                weather_data[target_date]["evening"]["forecasts"].append(forecast)
                            elif hour <= 3:
                                weather_data[target_date]["night"]["forecasts"].append(forecast)

                        formatted_weather_data = {}
                        for date, day_data in weather_data.items():
                            formatted_date = await format_date(date)
                            formatted_weather_data[formatted_date] = day_data
                            for time_period in ["morning", "day", "evening", "night"]:
                                forecasts = day_data[time_period]["forecasts"]
                                if forecasts:
                                    avg_temp = int(round(sum(f["temp"] for f in forecasts) / len(forecasts)))
                                    avg_feels_like = int(round(sum(f["temp_feels_like"] for f in forecasts) / len(forecasts)))
                                    avg_pressure = int(round(sum(f["pressure"] for f in forecasts) / len(forecasts)))
                                    avg_wind_speed = int(round(sum(f["wind_speed"] for f in forecasts) / len(forecasts)))
                                    wind_dir = int(round(sum(f["wind_direction"] for f in forecasts) / len(forecast)))

                                    weather_counts = Counter(f["weather"] for f in forecasts)
                                    most_common_weather = weather_counts.most_common(1)[0][0]

                                    icon_counts = Counter(f["icon"] for f in forecasts)
                                    most_common_icon = icon_counts.most_common(1)[0][0]

                                    day_data[time_period] = {
                                        "temp": f"+{avg_temp} °C" if avg_temp>0 else f"{avg_temp} °C",
                                        "temp_feels_like": f"+{avg_feels_like} °C" if avg_feels_like>0 else f"{avg_feels_like} °C",
                                        "pressure": await pressure_mmhg(avg_pressure),
                                        "wind_speed": avg_wind_speed,
                                        "weather": most_common_weather,
                                        "icon": most_common_icon,
                                        "wind_direction": await wind_direction(wind_dir),
                                        "forecast_count": len(forecasts)
                                    }

                        return formatted_weather_data
                    return None
                return None
                
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
                


if __name__=='__main__':
    print(asyncio.run(get_five_day_forecast_data(city_name=input('city: '))))

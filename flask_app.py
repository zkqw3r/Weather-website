from flask import Flask, render_template
from app.api import get_current_weather_data, get_five_day_forecast_data


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
async def home():
    return render_template("index.html")


@app.route("/weather/<city_name>")
async def search(city_name):
    current_weather_data = await get_current_weather_data(city_name=city_name)
    five_day_forecast_data = await get_five_day_forecast_data(city_name=city_name)
    
    if current_weather_data and five_day_forecast_data:
        return render_template('weather.html', 
                             cw_data=current_weather_data, 
                             fdf_data=five_day_forecast_data)
    elif current_weather_data:
        return render_template('weather.html', 
                             cw_data=current_weather_data)
    else:
        error = 'Город не найден'
        return render_template('weather.html', error=error)


@app.errorhandler(404)
def error404(error):
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)

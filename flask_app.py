from flask import Flask, render_template, request
from app.api import current_weather_data, wind_direction, pick_icon

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def index():
    city = None
    if request.method == 'POST':
        city = request.form.get('city_name')
    if city:
        try:
            weather, main, wind, cod, name = await current_weather_data(city_name=city)
            direction = await wind_direction(wind.get('deg'))
            img_link = f'https://openweathermap.org/img/wn/{str(weather[0].get("icon"))}@2x.png'
            pressure = int(round(main.get('pressure')*0.75006375541921))
            owm_icon_path = await pick_icon(weather)
            return render_template('index.html',
                                   weather=weather,
                                   wind=wind,
                                   direction=direction,
                                   main=main, 
                                   pressure=pressure,
                                   city=city,
                                   name=name,
                                   img_link=img_link,
                                   owm_icon_path=owm_icon_path,
                                   cod=cod)
        except:
            error = 'Город не найден'
            return render_template('index.html',
                                error=error)
    else:
        error = 'Введите город для получения данных'
    return render_template('index.html',
                           error=error)


if __name__ == '__main__':
    app.run(debug=True)

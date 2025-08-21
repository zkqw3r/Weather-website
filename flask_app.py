from flask import Flask, render_template
from app.api import current_weather_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
async def home():
    return render_template("index.html")


@app.route("/weather/<city_name>")
async def search(city_name):
    data = await current_weather_data(city_name=city_name)
    if data:
        return render_template('weather.html', data=data)
    else:
        error = 'Город не найден'
        return render_template('weather.html', error=error)


@app.errorhandler(404)
def error404(error):
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)

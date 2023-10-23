from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city=request.args.get('city')
    if not bool(city.strip()):    #check if city is an empty string
        city="Paris"
    
    weather_data=get_current_weather(city)
    if 'error' in weather_data:   #check if a city name is valid
        return render_template('city-not-found.html')
    return render_template(
        "weather.html",
        title=weather_data["location"]["name"],
        status=weather_data["current"]["condition"]["text"].capitalize(),
        temp=f"{weather_data['current']['temp_c']:.1f}",
        feels_like=f"{weather_data['current']['feelslike_c']:.1f}"
    )

if __name__=="__main__":
    serve(app,host="0.0.0.0",port=8000)


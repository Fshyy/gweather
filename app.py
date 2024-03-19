from flask import Flask, render_template, request
import requests
from datetime import datetime
from matplotlib import pyplot as plt
app = Flask(__name__)


@app.route('/')
def index():
    # x_time = [0,1,2,3,4,5,6]
    # y_temp = [18,15,13,9,8,8,11]
    # plt.plot(x_time,y_temp)
    # plt.savefig('test_chart')


    return render_template('home.html')


@app.route('/result', methods=["GET", "POST"])
def result():
    api_key = "b05f3500420020c6982dfa7baff61234"
    form_city = request.form.get('city')
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + form_city + "&APPID=" + api_key
    response = requests.get(url).json()
    print(url)

    weather_list = response.get("weather",)
    weather_one = weather_list[0]
    timezone = response.get("timezone")
    description = weather_one.get("description")
    temp_k = response.get("main", {}).get("temp")
    temp_c = int(temp_k) - 273.15
    wind_speed = response.get("wind", {}).get("speed")





    weather_dict = {
        'timezone': timezone,
        'description': description,
        'temp_k': temp_k,
        'temp_c': temp_c,
        'wind_speed': wind_speed
    }

    return render_template('result.html', response=response, weather_dict=weather_dict)


if __name__ == '__main__':
    app.run(debug=True)

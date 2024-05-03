from flask import Flask, render_template, request
import requests
from datetime import datetime
from matplotlib import pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    api_key = "b05f3500420020c6982dfa7baff61234"
    form_city = "Adelaide"
    url = "http://api.openweathermap.org/data/2.5/forecast?q=" + form_city + "&APPID=" + api_key
    response = requests.get(url).json()
    print(url)
    forecast_list = response["list"]
    print(forecast_list)


    forecast_data = []
    index = 0
    while index <len(forecast_list):

        dt_txt = forecast_list[index]["dt_txt"]
        temp = forecast_list[index]["main"]["temp"]
        desc = forecast_list[index]["weather"][0]["main"]
        icon = forecast_list[index]["weather"][0]["icon"]



        thisdict = {
            "dt_txt": dt_txt,
            "temp": temp,
            "desc": desc,
            "icon_url": "http://openweathermap.org/img/w/" + icon + ".png"
        }
        forecast_data.append(thisdict)
        index += 8
        print(forecast_data)



    return render_template('home.html', forecast_data=forecast_data)

if __name__ == '__main__':
    app.run(debug=True)

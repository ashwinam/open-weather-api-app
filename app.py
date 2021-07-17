import requests
import configparser
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def Weather_Dashboard():
    return render_template('index.html')


@app.route('/results',methods=['POST'])
def Weather_results():
    city_name = request.form['cityName']
    apiKey=get_api_key()
    data=get_weather_result(city_name,apiKey)
    temp="{0:.2f}".format(data['main']['temp'])
    feels_like="{0:.2f}".format(data['main']['feels_like'])
    weather=data['weather'][0]['main']
    location=data['name']
    return render_template('result.html',location=location,temp=temp,feels_like=feels_like,weather=weather)

# api key is coming from config.ini

def get_api_key():
    config=configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']
def get_weather_result(cityName,apiKey):
    apiUrl=f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&units=metric&appid={apiKey}"
    data=requests.get(apiUrl)
    return data.json()
if __name__=='__main__':
    app.run(debug=False)
    




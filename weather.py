from flask import Flask,render_template,request
import requests
app=Flask(__name__, template_folder='template')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=="POST":
       url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4178f99503d87843ee56d9ebd72fd510'
       city_name=request.form.get('city')
       r=requests.get(url.format(city_name)).json()
       weather={
          'city':city_name,
          'temperature':r['main']['temp'],
          'description':r['weather'][0]['description'],
          'icon':r['weather'][0]['icon'], 
        }
       return render_template("weather.html",weather=weather)
    else:   
        city="bina"
        url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4178f99503d87843ee56d9ebd72fd510'
        r=requests.get(url.format(city)).json()
        print(r)
        weather={
          'city':city,
          'temperature':r['main']['temp'],
          'description':r['weather'][0]['description'],
          'icon':r['weather'][0]['icon'], 
        }
        print(weather)
        return render_template("weather.html",weather=weather)

if __name__ == '__main__':  
  app.run(debug = False)
from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TENOR_API_KEY = os.getenv("TENOR_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Water."""
    return render_template('index.html')

@app.route('/fortune')
def fortune_form():
    return render_template('fortune_form.html')


@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_gender = request.args.get('gender')
    users_name = request.args.get('name') 
    users_city = request.args.get('city')
    fav_drink = request.args.get('drink')
    fav_movie = request.args.get('franchise')
    fortune = ""
    points = 0
    if users_city == "chicago":
        points += 2
    elif users_city == 'san francisco':
        points += 7
    elif users_city == 'louisville':
        points += 10
    elif users_city == 'new york':
        points += 4
    else:
        fortune = "you forgot to click anything! but you'll have a fantastic day"
        
    if fav_drink == "coffee":
        points += 2 
    elif fav_drink == "water":
        points += 8
    elif fav_drink == "tea":
        points += 5
    elif fav_drink == "orange juice":
        points += 3
    elif fav_drink == "sparkling water":
        points -=5
    elif fav_drink == "bourbon":
        points += 10
    else:
        print("you didn't pick a drink")
        
    if fav_movie == "lord of the rings":
        points += 9
    elif fav_movie == "fast and furious":
        points += 3
    elif fav_movie == "harry potter":
        points += 5
    elif fav_movie == "star wars":
        points += 7
    else:
        print("you didn't pick a movie")
    
        
    if points <= 0:
        fortune = "Be ready to open the door when opportunity knocks."
    elif points > 0 and points < 8:
        fortune = "someone is looking up to you. don't let that person down"
    elif points > 8 and points < 17:
        fortune = "enjoy yourself while you can"
    elif points == 17:
        fortune = "avoid taking unnecessary gambles"
    elif points < 27 and points > 17:
        fortune = "learn as much from joy as you do from pain"
    elif points == 29:
        fortune = "yeehaw!!!!"
    else:
        fortune = "error"
    
    
    
    
    return render_template("fortune_results.html", name=users_name, gender=users_gender, city=users_city, fortune=fortune, drink=fav_drink)
    #return "Hello " + users_name + "\n" + "you are a " + users_gender
    
@app.route('/weather')
def weather_page():
    return render_template("weather_form.html")
    
@app.route('/weather_results')
def weather_results_page():
    users_city = request.args.get('city')
    print(users_city)
    url = "http://api.openweathermap.org/data/2.5/weather?q="+users_city+"&appid=2608f679d4594364525f6c6cc2246c79"
    response = requests.get(url)
    response_json = response.json()
    print(response_json)
    main_data = response_json["main"]
    city_humidity = main_data["humidity"]
    temp_in_kelvin = main_data["temp"]
    temp_in_celsius = (temp_in_kelvin - 273.15)
    temp_in_celsius = int(round(temp_in_celsius))
    temp_in_farenheit = (temp_in_celsius * (9/5)) + 32
    return render_template("weather_results.html", city=users_city, temp=temp_in_farenheit, humidity=city_humidity)


    

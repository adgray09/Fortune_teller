from flask import Flask, render_template, request

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
    fortune = ""
    if users_city == "chicago" and fav_drink == 'coffee':
        fortune = "if you refuse to accept anything but the best, you very often get it"
    elif users_city == 'san francisco' and fav_drink == 'water' :
        fortune = "you cannot love life until you live the life you love"
    elif users_city == 'louisville' and fav_drink == 'sparkling water':
        fortune = "you are a fantastic human being"
    elif users_city == 'new york':
        fortune = "don't let all the people overshadow your greatness"
    elif users_city == "louisville":
        fortune = "yeehaw!"
    else:
        fortune = "you forgot to click anything! but you'll have a fantastic day"
        
    
    return render_template("fortune_results.html", name=users_name, gender=users_gender, city=users_city, fortune=fortune, drink=fav_drink)
    #return "Hello " + users_name + "\n" + "you are a " + users_gender

    

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')


@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_gender = request.args.get('gender')
    # ... etc

    if users_gender == 'male':
        print("you are a man")
    return render_template('fortune_results.html')
        
        
        
        
        
        

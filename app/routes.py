from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def homePage():
    five_like = [
        {'Music': "TOOL"},
        {'Food': "Tacos"},
        {'BOOK': "Name of the Wind"},
        {'Car' : "1967 lincoln continental"},
        {'MOVIE' : "The Crow"}
        ]


    return render_template('index.html', names=five_like)



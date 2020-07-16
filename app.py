# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model
# from flask import render_template
# from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/favorite_color')
def favorite_color():
    return render_template("favorite_color.html")
@app.route('/favorite_element', methods=['GET', 'POST'])
def favorite_element():
    user_color = request.form["user_color"]
    if user_color.lower() == "red":
        return render_template("favorite_element_red.html")
    elif user_color.lower() == "blue":
        return render_template("favorite_element_blue.html")
    elif user_color.lower() == "green":
        return render_template("favorite_element_green.html")
    elif user_color.lower() == "yellow":
        return render_template("favorite_element_yellow.html")
@app.route('/favorite_element_red')
def favorite_element_red():
    return render_template("favorite_element_red.html")
@app.route('/favorite_element_blue')
def favorite_element_blue():
    return render_template("favorite_element_blue.html")
@app.route('/favorite_element_green')
def favorite_element_green():
    return render_template("favorite_element_green.html")
@app.route('/favorite_element_yellow')
def favorite_element_yellow():
    return render_template("favorite_element_yellow.html")
@app.route('/results', methods=['GET', 'POST'])
def results():
    user_element = request.form["user_element"]
    user_pokemon = model.favorite_element(user_element)
    return render_template("results.html", user_pokemon = user_pokemon)

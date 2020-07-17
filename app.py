# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model
from datetime import datetime
# from flask import render_template
# from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/favorite_color')
def favorite_color():
    return render_template("favorite_color.html", time=datetime.now())


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
def Results():
    user_element = request.form["user_element"]
    user_pokemon = model.favorite_element(user_element)
    pokeList = ["Arbok", "Blastoise", "Butterfree", "Charizard", "Clefable", "Cofagrigus", "Darkrai", "Dragonite", "Eiscue", "Groudon", "Machamp", "Melmetal", "Mew", "Pikachu", "Rampardos", "Snorlax", "Tornadus", "Venusaur"]
    i = 0
    while i < len(pokeList):
        if pokeList[i].upper() == user_pokemon.upper() and i == 0:
            return render_template("Results(Arbok).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 1:
            return render_template("Results(Blastoise).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 2:
            return render_template("Results(Butterfree).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 3:
            return render_template("Results(Charizard).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 4:
            return render_template("Results(Clefable).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 5:
            return render_template("Results(Cofagrigus).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 6:
            return render_template("Results(Darkrai).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 7:
            return render_template("Results(Dragonite).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 8:
            return render_template("Results(Eiscue).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 9:
            return render_template("Results(Groudon).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 10:
            return render_template("Results(Machamp).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 11:
            return render_template("Results(Melmetal).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 12:
            return render_template("Results(Mew).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 13:
            return render_template("Results(Pikachu).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 14:
            return render_template("Results(Rampardos).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 15:
            return render_template("Results(Snorlax).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 16:
            return render_template("Results(Tornadus).html")
        else:
            i = i + 1
        if pokeList[i].upper() == user_pokemon.upper() and i == 17:
            return render_template("Results(Venusaur).html")
        else:
            i = i + 1

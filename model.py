red_elements = ["fire", "fighting", "fairy", "rock"]
red_pokemon = ["Charizard", "Machamp", "Clefable", "Rampardos"]
blue_elements = ["water", "psychic", "dark", "flying", "ice"]
blue_pokemon = ["Blastoise", "Mew", "Darkrai", "Tornadus", "Eiscue"]
green_elements = ["grass", "bug", "steel", "poison", "normal"]
green_pokemon = ["Bulbasaur", "Butterfree", "Melmetal", "Arbok", "Snorlax"]
yellow_elements = ["electric", "ghost", "dragon", "ground"]
yellow_pokemon = ["Pikachu", "Cofagrigus", "Dragonite", "Groudon"]


def favorite_element(element):
    for i in range(0, len(red_elements)):
        if red_elements[i].title() == element:
            return red_pokemon[i]
    for i in range(0, len(blue_elements)):
        if blue_elements[i].title() == element:
            return blue_pokemon[i]
    for i in range(0, len(green_elements)):
        if green_elements[i].title() == element:
            return green_pokemon[i]
    for i in range(0, len(yellow_elements)):
        if yellow_elements[i].title() == element:
            return yellow_pokemon[i]

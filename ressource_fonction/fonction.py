from ressource_objet.objets import*
from random import randint

print("dd")

def carac():
    """ Retourne un caractère aléatoire """
    n = randint(97, 125) # a -> 97
    if n == 123:
        return " "
    elif n == 124:
        return "."
    elif n == 125:
        return ","
    else:
        return chr(n)

print(carac())
from random import randint

def carac():
    """ Retourne un caractère aléatoire (Les 26 lettres minuscule de l'alphabet + espace + 2 caractères de ponctuation : '.' et ',')"""
    n = randint(97, 125)
    if n == 123:
        return " "
    elif n == 124:
        return "."
    elif n == 125:
        return ","
    else:
        return chr(n)
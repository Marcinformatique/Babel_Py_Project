from random import randint

def carac():
    """ Retourne un caractère aléatoire (Les 26 lettres minuscule de l'alphabet + espace + 2 caractères de ponctuation : '.' et ',')."""
    n = randint(97, 125)
    if n == 123:
        return " "
    elif n == 124:
        return "."
    elif n == 125:
        return ","
    else:
        return chr(n)
    
from ressource_objet.objets import Hexagone, NB_HEXAGONES
    
def create_And_Init_Babel() -> list[Hexagone]:
    l = []
    for i in range(NB_HEXAGONES):
        l += [Hexagone()]
        l[-1].initExagone()
    return l
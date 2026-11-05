from ressource_fonction.fonction import*
from ressource_objet.objets import*
# Avant la boucle principal : initialisation de la bibliothèque
etagere = Etageres()
etagere.initEtageres()
etagere.contenu[0].print_page(0)
babel = create_And_Init_Babel(1)
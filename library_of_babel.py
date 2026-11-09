from ressource_fonction.fonction import*
from ressource_objet.objets import*
# Avant la boucle principal : initialisation de la bibliothèque

etagere = Etageres()
etagere.initEtageres()
babel = create_And_Init_Babel(1)
no_page=0
recherche=""

while True:
    print("--------------------------------------------------------------------------------")
    babel[0].contenu[0].contenu[0].print_page(no_page,recherche)
    print(f"( 1/Changer d'hexagone | 2/Changer d'étagère | 3/Changer de livre | 4/ Changer de page | 5/Rechercher une citation )")
    reponse=int(input("Quel action: "))
    if reponse==4:
        page=int(input("Quelle page: "))
        if 0<=page<=NB_PAGES: no_page=page-1
    if reponse==5:
        recherche=input("Quelle citation voulez-vous rechercher dans cette page: ")

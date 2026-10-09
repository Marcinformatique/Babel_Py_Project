from ressource_fonction.fonction import*
NB_CHAR = 80
NB_LIGNES = 40
NB_PAGES = 410
NB_LIVRES = 32
NB_ETAGERES = 5
NB_HEXAGONES = 2

class Livres:
    def __init__(self):
        self.contenu=[[]] # 1ère dimension de la liste : les différentes pages | 2e dimension : les lignes contenant elle même une chaine de 80 caractères.
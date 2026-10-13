from ressource_fonction.fonction import*
NB_CHAR = 80
NB_LIGNES = 40
NB_PAGES = 410
NB_LIVRES = 32
NB_ETAGERES = 5
NB_HEXAGONES = 1
class Livres:
    def __init__(self):
        self.contenu=[[""]*NB_LIGNES]*NB_PAGES # 1ère dimension de la liste : les différentes pages | 2e dimension : les lignes contenant elle même une chaine de 80 caractères.
    
    def add_Contenu(self):
        """ Intitialiser un livre => placer tout les caractères """
        for page in range(NB_PAGES):
            for ligne in range(NB_LIGNES):
                for caractere in range(NB_CHAR):
                    self.contenu[page][ligne] += carac()
                    
    def print_page(self, no_page):
        """ Afficher le contenu d'une page """
        for ligne in range(NB_LIGNES):
            for caracter in range(NB_CHAR):
                print(self.contenu[no_page][ligne][caracter], end="")
            print()
 
class Etageres:
    def __init__(self):
        self.contenu = [Livres()]
        self.contenu = []
    def initEtageres(self):
        for livre in range(NB_LIVRES):
            self.contenu += [Livres()]
            self.contenu[livre].add_Contenu()
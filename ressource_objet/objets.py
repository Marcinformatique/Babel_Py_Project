from ressource_fonction.fonction import carac
NB_CHAR = 80
NB_LIGNES = 40
NB_PAGES = 1
NB_LIVRES = 32
NB_ETAGERES = 5
NB_HEXAGONES = 1
NB_RESSOURCES_INIT=NB_ETAGERES*NB_HEXAGONES*NB_LIVRES
nb_ressources_initie=0

VERT = "\033[32m"
RESET = "\033[0m"


class Livres:
    def __init__(self):
        self.contenu=[[""]*NB_LIGNES]*NB_PAGES # 1ère dimension de la liste : les différentes pages | 2e dimension : les lignes contenant elle même une chaine de 80 caractères.
    
    def add_Contenu(self):
        global nb_ressources_initie
        """ Intitialiser un livre => placer tout les caractères """
        for page in range(NB_PAGES):
            for ligne in range(NB_LIGNES):
                for caractere in range(NB_CHAR):
                    self.contenu[page][ligne] += carac()
        nb_ressources_initie+=1
        print(f"[ {round(nb_ressources_initie/NB_RESSOURCES_INIT*100,3)}% ]")
                    

    def print_page(self, no_page: int, recherche):
        """ Afficher le contenu d'une page """
        if recherche=="":
            for ligne in range(NB_LIGNES):
                for caracter in range(NB_CHAR):
                    print(self.contenu[no_page][ligne][caracter], end="")
                print()
        else:
            defil=0
            for ligne in range(NB_LIGNES):
                for caracter in range(NB_CHAR):
                    if ligne*NB_CHAR+(caracter+1)<=(NB_LIGNES*NB_CHAR)-len(recherche)+1:
                        for i in range(len(recherche)):
                            if self.contenu[no_page][ligne+(i+caracter)//NB_CHAR][(caracter+i)%NB_CHAR]==recherche[i]:
                                if i+1==len(recherche):
                                    defil=len(recherche)
                                continue
                            else:
                                break
                    if defil>0:
                        print(f"{VERT}{self.contenu[no_page][ligne][caracter]}{RESET}", end="")
                        defil-=1
                    else:
                        print(f"{self.contenu[no_page][ligne][caracter]}", end="")
                print()
                    
                    

        print(f"---------------- Page {no_page+1} / {NB_PAGES} ----------------")

 
class Etageres:
    def __init__(self):
        self.contenu = [Livres()]
        self.contenu = []
    def initEtageres(self):
        """ Intitialiser une étagère (la remplir de livre -> initialise les livres en question par la même) """
        for livre in range(NB_LIVRES):
            self.contenu += [Livres()] # Ajouter un livre
            self.contenu[livre].add_Contenu() # Initialiser le même livre

class Hexagone:
    def __init__(self):
        self.contenu = [Etageres()]
        self.contenu = []
    def initExagone(self):
        """ Initialiser un hexagone (remplir celui-ci et également initialiser le contenu des étagères => ce qui va donc initialiser les livres) """
        for i in range(NB_ETAGERES):
            self.contenu += [Etageres()]
            self.contenu[-1].initEtageres()
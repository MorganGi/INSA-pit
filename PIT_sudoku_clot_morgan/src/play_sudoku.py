from functools import partial
from grid import SudokuGrid
import sys

def affiche_grille():
    print(Partie_1.__str__())


def verif_saisie():
    
    ligne = int (input ("choisir la  ligne a modifier:")) - 1
    colonne = int (input ("choisir la  colonne a modifier:")) - 1
    v = int(input("Par quelle valeur voulez vous la remplacer ?"))
    try:
        Partie_1.write(ligne,colonne,v)

    except:
        print("\n*********Choisir un emplacement vide (0) *********")
        
    

if __name__=="__main__":
    flag = True
    start = True
    while flag:
        while start:
            Args = []
            for arg in sys.argv:
                Args.append(str(arg))
            print("ARGUMENTS LU DANS LA COMMANDE",Args, len(Args))
            if len(Args) == 3:

                Partie_1 = SudokuGrid(SudokuGrid.from_file(str(Args[1]),int(Args[2])))
                start=False
                
            else:
                choix= input("Entre votre grille : ")
                Partie_1 = SudokuGrid(choix)
                start=False
        
        affiche_grille()
        verif_saisie()
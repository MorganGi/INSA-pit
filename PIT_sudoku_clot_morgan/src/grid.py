#-*-coding: utf8-*-

class SudokuGrid:
    """Cette classe représente une grille de Sudoku.
    Toutes ces méthodes sont à compléter en vous basant sur la documentation fournie en docstring.
    """

    def __init__(self, initial_values_str):
        """À COMPLÉTER!
        Ce constructeur initialise une nouvelle instance de la classe SudokuGrid.
        Il doit effectuer la conversation de chaque caractère de la chaîne en nombre entier,
        et lever une exception (ValueError) si elle ne peut pas être interprétée comme une grille de Sudoku.
        :param initial_values_str: Une chaîne de caractères contenant **exactement 81 chiffres allant de 0 à 9**,
            où ``0`` indique une case vide
        :type initial_values_str: str
        """
        
        self.grid = [[0] * 9 for i in range(9)]
        compteur = 0

        try:
            self.initial_values_str = initial_values_str
            if len(self.initial_values_str) != 81 :
                print("chaine != 81")
                raise ValueError()

            else:
                for lignes in range(9) :
                    for colones in range(9):
                            self.grid[lignes][colones] = (int(self.initial_values_str[compteur]))
                            compteur += 1  
        except:
            print("Erreur venant du try")
            raise ValueError()
                
        

    @staticmethod
    def from_file(filename, line):
        """À COMPLÉTER!
        Cette méthode de classe (ou méthode statique) crée une nouvelle instance de grille de Sudoku
        à partir d'une ligne contenue dans un fichier.

        :param filename: Chemin d'accès vers le fichier à lire
        :param line: Numéro de la ligne à lire
        :type filename: str
        :type line: int
        :return: La grille de Sudoku correspondant à la ligne donnée dans le fichier donné
        :rtype: SudokuGrid
        """
        
        with open(filename,"r+") as file:
                data=file.readlines()[line][:-1]
        return data
                                 
        

    @staticmethod
    def from_stdin():
        """À COMPLÉTER!
        Cette méthode de classe crée une nouvelle instance de grille de Sudoku
        à partir d'une ligne lu depuis l'entrée standard (saisie utilisateur).
        *Variante avancée: Permettez aussi de «piper» une ligne décrivant un Sudoku.*
        :return: La grille de Sudoku correspondant à la ligne donnée par l'utilisateur
        :rtype: SudokuGrid
        """
        grille = input("Entrez votre grille de sudoku : ")
        return SudokuGrid(grille)
        raise NotImplementedError()

    def __str__(self):
        """À COMPLÉTER!
        Cette méthode convertit une grille de Sudoku vers un format texte pour être affichée.
        :return: Une chaîne de caractère (sur plusieurs lignes...) représentant la grille
        :rtype: str
        """
        
        grille_str=""
        for lignes in range(9):
            for col in range(9):
                grille_str = grille_str + str(self.grid[lignes][col])
            grille_str = grille_str + "\n"
        
        return grille_str
        raise NotImplementedError()


    def get_row(self, i):
        """À COMPLÉTER!
        Cette méthode extrait une ligne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param i: Numéro de la ligne à extraire, entre 0 et 8
        :type i: int
        :return: La liste des valeurs présentes à la ligne donnée
        :rtype: list of int
        """
        for col in range(9):
            lignes= self.grid[i]
        return lignes
        raise NotImplementedError()


    def get_col(self, j):
        """À COMPLÉTER!
        Cette méthode extrait une colonne donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param j: Numéro de la colonne à extraire, entre 0 et 8
        :type j: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """
        li_return = []
        for lignes in self.grid:
            li_return.append(lignes[j])
        
        return li_return
        raise NotImplementedError()

    def get_region(self, reg_row, reg_col):
        """À COMPLÉTER!
        Cette méthode extrait les valeurs présentes dans une région donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param reg_row: Position verticale de la région à extraire, **entre 0 et 2**
        :param reg_col: Position horizontale de la région à extraire, **entre 0 et 2**
        :type reg_row: int
        :type reg_col: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """
        row=[]
        col=[]
        for lignes in range(3):
            row.append(self.grid[reg_row*3 + lignes])
        for cols in row:
            for i in range(3):
                col.append(cols[reg_col*3 + i])
        return col
        raise NotImplementedError()

    def get_empty_pos(self):
        """À COMPLÉTER!
        Cette méthode renvoit les positions des cases vides dans la grille de Sudoku,
        sous la forme de tuples ``(i,j)`` où ``i`` est le numéro de ligne et ``j`` le numéro de colonne.
        *Variante avancée: Renvoyez un générateur sur les tuples de positions ``(i,j)`` au lieu d'une liste*
        :return: La liste des positions des cases vides dans la grille
        :rtype: list of tuple of int
        """
        li_tuples=[]
        for lignes in range(9):
            for cols in range(9):
                if self.grid[lignes][cols] == 0:
                    li_tuples.append((lignes,cols))
        return li_tuples

        raise NotImplementedError()

    def write(self, i, j, v):
        """À COMPLÉTER!
        Cette méthode écrit la valeur ``v`` dans la case ``(i,j)`` de la grille de Sudoku.
        *Variante avancée: Levez une exception si ``i``, ``j`` ou ``v``
        ne sont pas dans les bonnes plages de valeurs*
        *Variante avancée: Ajoutez un argument booléen optionnel ``force``
        qui empêche d'écrire sur une case non vide*
        :param i: Numéro de ligne de la case à mettre à jour, entre 0 et 8
        :param j: Numéro de colonne de la case à mettre à jour, entre 0 et 8
        :param v: Valeur à écrire dans la case ``(i,j)``, entre 1 et 9
        """
        try:
            
            if (i,j) in self.get_empty_pos():
                if v in [1,2,3,4,5,6,7,8,9]:
                    self.grid[i][j] = v
                else :
                    raise ValueError()
            else:
                raise ValueError()
            
        except:
            raise IndexError()
            raise NotImplementedError()


    def copy(self):
        """À COMPLÉTER!
        Cette méthode renvoie une nouvelle instance de la classe SudokuGrid,
        qui doit être une copie **indépendante** de la grille de Sudoku.
        *Variante avancée: vous pouvez utiliser ``self.__new__(self.__class__)``
        pour court-circuiter l'appel à ``__init__`` et manuellement initialiser les attributs de la copie.*
        :return: Une copie de la grille courrante
        :rtype: SudokuGrid
        """    
        return SudokuGrid(self.initial_values_str.__str__())
        raise NotImplementedError()

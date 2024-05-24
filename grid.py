import random
from adversaire import Adversaire 
class Grid:
    def __init__(self, largeur, joueur1, joueur2):
        self.largeur = largeur
        self.tour = 0
        self.grid = []
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.adversaire = Adversaire(self)  # Initialisation de la classe Adversaire

    def initialise_grid(self):
        for i in range(self.largeur):
            self.grid.append([])
            for _ in range(self.largeur):
                self.grid[i].append(" ")
        return self.grid

    def afficher_grid(self):
        print(f"\n\n\n||TOUR {self.tour}|| \n")
        for colonne in self.grid:
            ligne = ""
            for element in colonne:
                ligne += f"|{element}"
            print(f"{ligne}|")

    def get_diag_1(self):
        return [self.grid[i][i] for i in range(self.largeur)]

    def get_diag_2(self):
        return [self.grid[i][self.largeur - i - 1] for i in range(self.largeur)]

    def get_columns(self):
        return [[self.grid[i][j] for i in range(self.largeur)] for j in range(self.largeur)]

    def get_lines(self):
        return [list(self.grid[i]) for i in range(self.largeur)]

    def jouer(self, x, y):
        symbole = "O" if self.tour % 2 == 0 else "X"
        self.grid[x][y] = symbole
        self.tour += 1

        victory = True
        for element in self.grid[x]:
            if element != symbole:
                victory = False
                break
        if not victory:
            victory = all(self.grid[i][y] == symbole for i in range(self.largeur))

        if self.grid[1][1] == symbole and not victory:
            victory = all(self.grid[i][i] == symbole for i in range(self.largeur)) or \
                      all(self.grid[i][self.largeur - i - 1] == symbole for i in range(self.largeur))

        return victory

    def case_is_free(self, x, y):
        return self.grid[x][y] == " "

    def get_tour(self):
        return self.tour

    def get_joueur(self):
        return self.joueur1 if self.tour % 2 == 0 else self.joueur2

    @staticmethod
    def is_parsable(an_input):
        try:
            int(an_input)
            return True
        except ValueError:
            return False

    def is_valid_in_grid(self, choice):
        return 0 <= choice < self.largeur

    def playable_cases(self):
        playable = []
        for colonne in range(self.largeur):
            for line in range(self.largeur):
                if self.grid[colonne][line] == " ":
                    playable.append((colonne,line))
        return playable

    def free_cases(self):
        free = []
        for colonne in range(self.largeur):
            for line in range(self.largeur):
                if self.grid[colonne][line] == " ":
                    free.append((colonne,line))
        if self.tour == 0:
            free.remove((1,1))
        return free

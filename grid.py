import random
class Grid:
    def __init__(self,largeur,joueur1,joueur2):
        self.largeur = largeur
        self.tour = 0
        self.grid = []
        self.joueur1 = joueur1
        self.joueur2 = joueur2

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
        return list(
            [self.grid[0][0],
            self.grid[1][1],
            self.grid[2][2]]
        )

    def get_diag_2(self):
        return list(
           [ self.grid[0][2],
            self.grid[1][1],
            self.grid[2][0]]
        )

    def get_columns(self):
        c1 = list(
                [self.grid[0][0],
                self.grid[1][0],
                self.grid[2][0]]
            )
        c2 = list(
               [ self.grid[0][1],
                self.grid[1][1],
                self.grid[2][1]]
            )
        c3 = list(
            [self.grid[0][2],
            self.grid[1][2],
            self.grid[2][2]]
        )
        return list([c1,c2,c3])

    def get_lines(self):
        l1 = list(self.grid[0])
        l2 = list(self.grid[1])
        l3 = list(self.grid[2])
        return list([l1,l2,l3])

    def jouer(self,x,y):
        if self.tour % 2 == 0:
            symbole = "O"
        else:
            symbole = "X"
        self.grid[x][y] = symbole
        self.tour = self.tour + 1

        victory = True
        for element in self.grid[x]:
            if element != symbole:
                victory = False
        if victory == False:
            victory = True
            for i in range(self.largeur):
                if self.grid[i][y] != symbole:
                    victory = False
                    break
        if self.grid[1][1] == symbole:
            if victory == False:
                victory = True
                for i in range(self.largeur):
                    if self.grid[i][i] != symbole:
                        victory = False
                        break
            if victory == False:
                victory = True
                for i in range(self.largeur):
                    case = self.largeur-i-1
                    if self.grid[i][case] != symbole:
                        victory = False
                        break
        return victory

    def case_is_free(self,x,y):
        if self.grid[x][y] == " ":
            return True
        else:
            return False

    def get_tour(self):
        return self.tour

    def get_joueur(self):
        if self.tour % 2 == 0:
            return self.joueur1
        else:
            return self.joueur2

    def is_parsable(an_input):
        try:
            int(an_input)
            return True
        except:
            return False

    def is_valid_in_grid(self,choice):
        if 0 <= choice < self.largeur:
            return True
        return False

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

    def detect_danger(self):
        if self.tour % 2 == 0:
            danger_symbole = "X"
        else:
            danger_symbole = "O"
        dangers = []
        diag_1 = self.get_diag_1()
        if(diag_1.count(danger_symbole) == 2 and " " in diag_1):
            dangers.append((diag_1.index(' '),diag_1.index(' ')))
        diag_2 = self.get_diag_2()
        if(diag_2.count(danger_symbole) == 2 and " " in diag_2):
             dangers.append((diag_2.index(' '),2-diag_2.index(' ')))
        lines = self.get_lines()
        for i in range (3):
            if lines[i].count(danger_symbole) == 2 and " " in lines[i]:
                 dangers.append((i,lines[i].index(' ')))
        columns = self.get_columns()
        for i in range (3):
            if columns[i].count(danger_symbole) == 2 and " " in columns[i]:
                 dangers.append((columns[i].index(' '),i))
        return dangers

    def detect_victory(self):
        if self.tour % 2 == 0:
            danger_symbole = "O"
        else:
            danger_symbole = "X"
        dangers = []
        diag_1 = self.get_diag_1()
        if(diag_1.count(danger_symbole) == 2 and " " in diag_1):
            dangers.append((diag_1.index(' '),diag_1.index(' ')))
        diag_2 = self.get_diag_2()
        if(diag_2.count(danger_symbole) == 2 and " " in diag_2):
             dangers.append((diag_2.index(' '),2-diag_2.index(' ')))
        lines = self.get_lines()
        for i in range (3):
            if lines[i].count(danger_symbole) == 2 and " " in lines[i]:
                 dangers.append((i,lines[i].index(' ')))
        columns = self.get_columns()
        for i in range (3):
            if columns[i].count(danger_symbole) == 2 and " " in columns[i]:
                 dangers.append((columns[i].index(' '),i))
        return dangers
    
    def adversaire(self):

        victory = self.detect_victory()
        if len(victory) > 0:
            return (victory[0][0], victory[0][1])
        dangers = self.detect_danger()
        if len(dangers) > 0:
            return (dangers[0][0], dangers[0][1])
        else:
            free = self.free_cases()
            if (1,1) in free:
                return (1,1)
            choice = random.randint(0, len(free)-1)
            print(f"free case : {free}")
            print(f"random choice : {choice}")
            return free[choice]

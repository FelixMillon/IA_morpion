import random

class Adversaire:
    def __init__(self, grid):
        self.grid = grid

    def detect_danger(self):
        danger_symbole = "X" if self.grid.tour % 2 == 0 else "O"
        dangers = []
        diag_1 = self.grid.get_diag_1()
        if diag_1.count(danger_symbole) == 2 and " " in diag_1:
            dangers.append((diag_1.index(' '), diag_1.index(' ')))
        diag_2 = self.grid.get_diag_2()
        if diag_2.count(danger_symbole) == 2 and " " in diag_2:
            dangers.append((diag_2.index(' '), 2 - diag_2.index(' ')))
        lines = self.grid.get_lines()
        for i in range(3):
            if lines[i].count(danger_symbole) == 2 and " " in lines[i]:
                dangers.append((i, lines[i].index(' ')))
        columns = self.grid.get_columns()
        for i in range(3):
            if columns[i].count(danger_symbole) == 2 and " " in columns[i]:
                dangers.append((columns[i].index(' '), i))
        return dangers

    def detect_victory(self):
        victory_symbole = "O" if self.grid.tour % 2 == 0 else "X"
        victories = []
        diag_1 = self.grid.get_diag_1()
        if diag_1.count(victory_symbole) == 2 and " " in diag_1:
            victories.append((diag_1.index(' '), diag_1.index(' ')))
        diag_2 = self.grid.get_diag_2()
        if diag_2.count(victory_symbole) == 2 and " " in diag_2:
            victories.append((diag_2.index(' '), 2 - diag_2.index(' ')))
        lines = self.grid.get_lines()
        for i in range(3):
            if lines[i].count(victory_symbole) == 2 and " " in lines[i]:
                victories.append((i, lines[i].index(' ')))
        columns = self.grid.get_columns()
        for i in range(3):
            if columns[i].count(victory_symbole) == 2 and " " in columns[i]:
                victories.append((columns[i].index(' '), i))
        return victories

    def next_move(self):
        victory = self.detect_victory()
        if victory:
            return victory[0]
        danger = self.detect_danger()
        if danger:
            return danger[0]
        free = self.grid.free_cases()
        if (1, 1) in free:
            return (1, 1)
        return random.choice(free)

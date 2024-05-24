from grid import Grid
from pymongo import MongoClient
from datetime import datetime
import uuid
import bson
import re

client = MongoClient('mongodb://localhost:27017/')
db = client.morpion
collection = db.parties

largeur = 3

print("joueur 1")
joueur1 = input()
print("joueur 2")
joueur2 = input()

grid = Grid(
    largeur=largeur,
    joueur1=joueur1,
    joueur2=joueur2
)

partie = {}
victorious = None
Grid.initialise_grid(grid)

victory = False
while not victory:
    tour = Grid.get_tour(grid)
    joueur = Grid.get_joueur(grid)
    print(f"Tour {tour}")
    print(f"Au tour de {joueur}")
    is_valid = False
    if not joueur.startswith("IA"):
        while not is_valid:
            is_valid_line = False
            is_valid_column = False
            while not is_valid_line:
                print("choose the line: ")
                line = input()
                if Grid.is_parsable(line):
                    line = int(line) - 1
                    is_valid_line = Grid.is_valid_in_grid(grid,line)
                    if not is_valid_line:
                        print(f"choose a number between 1 and {largeur}")
                else:
                    print(f"choose a number between 1 and {largeur}")
            while not is_valid_column:
                print("choose the column: ")
                column = input()
                if Grid.is_parsable(column):
                    column = int(column) - 1
                    is_valid_column = Grid.is_valid_in_grid(grid,column)
                    if not is_valid_column:
                        print(f"choose a number between 1 and {largeur}")
                else:
                    print(f"choose a number between 1 and {largeur}")
            if(
                tour == 0
                and line == 1
                and column == 1
            ):
                print("impossible de jouer le centre au premier tour")
            else:
                is_valid = Grid.case_is_free(grid,line,column)
                if not is_valid:
                    print("case not free")
    else:
        line, column = Grid.adversaire(grid)
    victory = Grid.jouer(grid,line,column)
    Grid.afficher_grid(grid)
    if tour >= 8 and not victory:
        print("match nul")
        break

    partie[str(tour)] = {}
    partie[str(tour)]["line"] = line
    partie[str(tour)]["column"] = column
    partie[str(tour)]["victory"] = victory
    partie[str(tour)]['timestamp'] = datetime.now()
    partie[str(tour)]['joueur'] = joueur
if victory:
    victorious = joueur
    print(f'Victoire du joueur {joueur}')
    

partie["_id"]: uuid.uuid4()
partie["victorious"] = victorious

collection.insert_one(partie)
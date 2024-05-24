from grid import Grid
from pymongo import MongoClient
from datetime import datetime
import uuid

client = MongoClient('mongodb://localhost:27017/')
db = client.morpion
collection = db.parties

largeur = 3

for i in range(50):
    print("Joueur 1:")
    joueur1 = "IA1"
    print("Joueur 2:")
    joueur2 = "IA2"

    grid = Grid(
        largeur=largeur,
        joueur1=joueur1,
        joueur2=joueur2
    )

    partie = {}
    victorious = None
    grid.initialise_grid()

    victory = False
    while not victory:
        tour = grid.get_tour()
        joueur = grid.get_joueur()
        print(f"Tour {tour}")
        print(f"Au tour de {joueur}")
        is_valid = False

        if not joueur.startswith("IA"):
            while not is_valid:
                is_valid_line = False
                is_valid_column = False

                while not is_valid_line:
                    print("Choose the line: ")
                    line = input()
                    if Grid.is_parsable(line):
                        line = int(line) - 1
                        is_valid_line = grid.is_valid_in_grid(line)
                        if not is_valid_line:
                            print(f"Choose a number between 1 and {largeur}")
                    else:
                        print(f"Choose a number between 1 and {largeur}")

                while not is_valid_column:
                    print("Choose the column: ")
                    column = input()
                    if Grid.is_parsable(column):
                        column = int(column) - 1
                        is_valid_column = grid.is_valid_in_grid(column)
                        if not is_valid_column:
                            print(f"Choose a number between 1 and {largeur}")
                    else:
                        print(f"Choose a number between 1 et {largeur}")

                if tour == 0 and line == 1 and column == 1:
                    print("Impossible de jouer le centre au premier tour")
                else:
                    is_valid = grid.case_is_free(line, column)
                    if not is_valid:
                        print("Case not free")
        else:
            line, column = grid.adversaire.next_move()

        victory = grid.jouer(line, column)
        grid.afficher_grid()

        if tour >= 8 and not victory:
            print("Match nul")
            break

        partie[str(tour)] = {
            "line": line,
            "column": column,
            "victory": victory,
            "timestamp": datetime.now(),
            "joueur": joueur
        }

    if victory:
        victorious = joueur
        print(f'Victoire du joueur {joueur}')

    partie["_id"] = str(uuid.uuid4())
    partie["victorious"] = victorious

    collection.insert_one(partie)

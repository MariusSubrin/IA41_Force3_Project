"""Principe de jeu ?
2 joueurs
carré de 9 cases
3 Pions noir et 2 pions blancs
Il faut aligner nos trois pions pour gagner
Si la case vide est sur un côté : 
    le joueur peut déplacer 2 carrés DE SON CHOIX d'un coup
On ne peux jamais revenir à la position juste avant, 
    donc pas de risque si 2 carrés déplacés par l'autre joueur

"""

"""Consigne ?
Rapport pour le 6 Janvier
Soutenance entre le 7 et 1à Janvier
Algo Min-Max avec ou sans élagage Alpha-Bétâ
"""

#On définit la création d'une case
def case (has_square, piece = "nothing") :
    return [has_square, piece]

#On initialise le jeu
def init_game():
    board = [
        [case(True),  case(True),  case(True)],
        [case(True),  case(False), case(True)],
        [case(True),  case(True),  case(True)]
    ]
    return board

def modif_case (case, has_square, piece) :
    case[0] = has_square
    case[1] = piece
    return case

def poser_piece(board, x, y, which_piece):
    """
    Pose un pion sur la case (x, y) si la case contient un carré
    et n'a pas déjà de pion.
    """
    if board[x][y][0] == True and board[x][y][1] == "nothing":
        board[x][y][1] = which_piece
        return True  # succès
    else:
        return False  # impossible de poser

#comme le joueur sélection là ou il veut déplacer son carré ou bien son pion, il n'y a pas besoin de vérification de sorties de bordures

def verif_modif_square(board, a, b, c, d):
    """
    Vérifie si un carré de (a,b) peut aller à (c,d)
    - doit y avoir un carré au départ
    - la case d'arrivée ne doit pas avoir de carré
    """
    start = board[a][b]
    end = board[c][d]
    return start[0] == True and end[0] == False

# Vérification si un pion peut être déplacé
def verif_modif_piece(board, a, b, c, d):
    """
    Vérifie si un pion de (a,b) peut aller à (c,d)
    - il doit y avoir un pion à déplacer
    - la case d'arrivée doit avoir un carré et aucun pion
    """
    start = board[a][b]
    end = board[c][d]
    return start[1] != "nothing" and end[0] == True and end[1] == "nothing"

# Vérifier si un joueur a gagné
def is_there_a_winner(board):
    """
    Vérifie toutes les lignes, colonnes et diagonales
    pour un alignement de trois pions identiques
    """
    for i in range(3):
        # lignes
        if board[i][0][1] != "nothing" and board[i][0][1] == board[i][1][1] == board[i][2][1]:
            return True
        # colonnes
        if board[0][i][1] != "nothing" and board[0][i][1] == board[1][i][1] == board[2][i][1]:
            return True
    # diagonale principale
    if board[0][0][1] != "nothing" and board[0][0][1] == board[1][1][1] == board[2][2][1]:
        return True
    # diagonale secondaire
    if board[0][2][1] != "nothing" and board[0][2][1] == board[1][1][1] == board[2][0][1]:
        return True
    return False

# Affichage du plateau (optionnel pour test)
def print_board(board):
    """
    Affiche le plateau avec :
    - . = case vide
    - W = pion blanc
    - B = pion noir
    """
    for row in board:
        row_str = ""
        for sq, piece in row:
            if piece == "white":
                row_str += " W "
            elif piece == "black":
                row_str += " B "
            else:
                row_str += " . " if sq else "   "
        print(row_str)
    print("\n")


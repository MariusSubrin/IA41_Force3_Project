from game_core import *

while is_there_a_winner != True :
    





#-------------------------------

if __name__ == "__main__":
    board = init_game()
    print("Board initial :")
    print_board(board)

    # On modifie une case, par exemple la case (0,0)
    print("\nOn modifie la case (0,0) pour mettre un pion white :")
    modif_case(board[0][0], True, "white")
    print_board(board)

    # autre test : changer la case centrale pour remettre un carré
    print("\nOn modifie la case centrale (1,1) pour remettre un carré avec rien dessus :")
    modif_case(board[1][1], True, "nothing")
    print_board(board)
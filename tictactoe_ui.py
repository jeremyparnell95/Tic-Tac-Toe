import tictactoe_logic
import tictactoe_ai

def start_turn():
    while True:
        start = raw_input("Who is going to start, X or O: ")
        if start == "X":
            return 1
        elif start == "O":
            return 2
        else:
            print("That is not one of the viable options, please choose again: ")
            print
            continue

def get_opponent(turn):
    if turn == 1:
        opponent = 2
    else:
        opponent = 1
    return opponent
        
def get_winner(winner):
    if winner == 1:
        print("The winner is FIRST PLAYER")
    elif winner == 2:
        print("The winner is SECOND PLAYER")
    else:
        print("NO ONE won the game")
    print

def check_mode():
    while True:
        players = raw_input("1 Playern or 2 Players (1 or 2): ")
        if players == "1":
            return True
        elif players == "2":
            return False
        else:
            print("That is not one of the viable options, please choose again: ")
            print
            continue

                
if __name__ == "__main__":
    print
    ai = check_mode()
    turn = start_turn()
    opponent = get_opponent(turn)
    t = tictactoe_logic.tictactoe(turn)
    t.new_board()
    while True:
        print
        t.print_board()
        print
        turn = t.turn()
        while True:
            if turn != opponent or (turn == opponent and ai == False):
                try:
                    print("It is {} player's turn. If you wish to start over, please type in REDO:".format(turn))
                    print
                    row = raw_input("what row would you like: ")
                    if row.upper().strip() == "REDO":
                        print
                        continue
                    column = raw_input("what column would you like: ")
                    if column.upper().strip() == "REDO":
                        print
                        continue
                    t.move(int(row),int(column))
                    t.check_board()
                    break
                except:
                    print
                    print("ERROR: YOU CANNOT CHOOSE THIS SPOT, PLEASE CHOOSE A NEW ONE...")
                    print
                    print("Player {} it is your turn again:".format(turn))
                    continue
            else:
                t._board = tictactoe_ai.ttt_ai(opponent,t._board) 
                t.check_diagonal()
                for val in range(3):
                    t.check_diagonal()
                    t.check_horizontal(val)
                    t.check_vertical(val)
                break
        
        winner = t.winner()
        if winner == 1 or winner == 2 or winner == 3:
            break
        else:
            t.change_turn()
    print                  
    t.print_board()
    print
    get_winner(winner)

        

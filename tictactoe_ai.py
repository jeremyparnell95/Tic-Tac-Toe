#tictactoe

def ttt_ai(opponent,board):
    rows = 3
    columns = 3
    ai_turn = opponent
    if ai_turn == 1:
    	ai_opponent = 2
    else:
    	ai_opponent = 1
    boardstate = board

    if boardstate[0][1] == ai_turn and boardstate[0][2] == ai_turn and boardstate[0][0] == 0:
    	boardstate[0][0] = ai_turn
    elif boardstate[0][0] == ai_turn and boardstate[0][2] == ai_turn and boardstate[0][1] == 0:
    	boardstate[0][1] = ai_turn
    elif boardstate[0][0] == ai_turn and boardstate[0][1] == ai_turn and boardstate[0][2] == 0:
    	boardstate[0][2] = ai_turn

    elif boardstate[1][1] == ai_turn and boardstate[1][2] == ai_turn and boardstate[1][0] == 0:
    	boardstate[1][0] = ai_turn
    elif boardstate[1][0] == ai_turn and boardstate[1][2] == ai_turn and boardstate[1][1] == 0:
    	boardstate[1][1] = ai_turn
    elif boardstate[1][0] == ai_turn and boardstate[1][1] == ai_turn and boardstate[1][2] == 0:
    	boardstate[1][2] = ai_turn

    elif boardstate[2][1] == ai_turn and boardstate[2][2] == ai_turn and boardstate[2][0] == 0:
    	boardstate[2][0] = ai_turn
    elif boardstate[2][0] == ai_turn and boardstate[2][2] == ai_turn and boardstate[2][1] == 0:
    	boardstate[2][1] = ai_turn
    elif boardstate[2][0] == ai_turn and boardstate[2][1] == ai_turn and boardstate[2][2] == 0:
    	boardstate[2][2] = ai_turn

    elif boardstate[1][0] == ai_turn and boardstate[2][0] == ai_turn and boardstate[0][0] == 0:
    	boardstate[0][0] = ai_turn
    elif boardstate[0][0] == ai_turn and boardstate[2][0] == ai_turn and boardstate[1][0] == 0:
    	boardstate[1][0] = ai_turn
    elif boardstate[0][0] == ai_turn and boardstate[1][0] == ai_turn and boardstate[2][0] == 0:
    	boardstate[2][0] = ai_turn

    elif boardstate[1][1] == ai_turn and boardstate[2][1] == ai_turn and boardstate[0][1] == 0:
    	boardstate[0][1] = ai_turn
    elif boardstate[0][1] == ai_turn and boardstate[2][1] == ai_turn and boardstate[1][1] == 0:
    	boardstate[1][1] = ai_turn
    elif boardstate[0][1] == ai_turn and boardstate[1][1] == ai_turn and boardstate[2][1] == 0:
    	boardstate[2][1] = ai_turn

    elif boardstate[1][2] == ai_turn and boardstate[2][2] == ai_turn and boardstate[0][2] == 0:
    	boardstate[0][2] = ai_turn
    elif boardstate[0][2] == ai_turn and boardstate[2][2] == ai_turn and boardstate[1][2] == 0:
    	boardstate[1][2] = ai_turn
    elif boardstate[0][2] == ai_turn and boardstate[1][2] == ai_turn and boardstate[2][2] == 0:
    	boardstate[2][2] = ai_turn

    elif boardstate[0][0] == ai_turn and boardstate[1][1] == ai_turn and boardstate[2][2] == 0:
    	boardstate[2][2] = ai_turn
    elif boardstate[1][1] == ai_turn and boardstate[2][2] == ai_turn and boardstate[0][0] == 0:
    	boardstate[0][0] = ai_turn
    elif boardstate[0][0] == ai_turn and boardstate[2][2] == ai_turn and boardstate[1][1] == 0:
    	boardstate[1][1] = ai_turn

    elif boardstate[0][2] == ai_turn and boardstate[1][1] == ai_turn and boardstate[2][0] == 0:
    	boardstate[2][0] = ai_turn
    elif boardstate[1][1] == ai_turn and boardstate[2][0] == ai_turn and boardstate[0][2] == 0: 
    	boardstate[0][2] = ai_turn
    elif boardstate[0][2] == ai_turn and boardstate[2][0] == ai_turn and boardstate[1][1] == 0:
    	boardstate[1][1] = ai_turn

    #defense
    elif boardstate[0][1] == ai_opponent and boardstate[0][2] == ai_opponent and boardstate[0][0] == 0:
    	boardstate[0][0] = ai_turn
    elif boardstate[0][0] == ai_opponent and boardstate[0][2] == ai_opponent and boardstate[0][1] == 0:
    	boardstate[0][1] = ai_turn
    elif boardstate[0][0] == ai_opponent and boardstate[0][1] == ai_opponent and boardstate[0][2] == 0:
    	boardstate[0][2] = ai_turn

    elif boardstate[1][1] == ai_opponent and boardstate[1][2] == ai_opponent and boardstate[1][0] == 0:
    	boardstate[1][0] = ai_turn
    elif boardstate[1][0] == ai_opponent and boardstate[1][2] == ai_opponent and boardstate[1][1] == 0:
    	boardstate[1][1] = ai_turn
    elif boardstate[1][0] == ai_opponent and boardstate[1][1] == ai_opponent and boardstate[1][2] == 0:
    	boardstate[1][2] = ai_turn

    elif boardstate[2][1] == ai_opponent and boardstate[2][2] == ai_opponent and boardstate[2][0] == 0:
    	boardstate[2][0] = ai_turn
    elif boardstate[2][0] == ai_opponent and boardstate[2][2] == ai_opponent and boardstate[2][1] == 0:
    	boardstate[2][1] = ai_turn
    elif boardstate[2][0] == ai_opponent and boardstate[2][1] == ai_opponent and boardstate[2][2] == 0:
    	boardstate[2][2] = ai_turn

    elif boardstate[1][0] == ai_opponent and boardstate[2][0] == ai_opponent and boardstate[0][0] == 0:
    	boardstate[0][0] = ai_turn
    elif boardstate[0][0] == ai_opponent and boardstate[2][0] == ai_opponent and boardstate[1][0] == 0:
    	boardstate[1][0] = ai_turn
    elif boardstate[0][0] == ai_opponent and boardstate[1][0] == ai_opponent and boardstate[2][0] == 0:
    	boardstate[2][0] = ai_turn

    elif boardstate[1][1] == ai_opponent and boardstate[2][1] == ai_opponent and boardstate[0][1] == 0:
    	boardstate[0][1] = ai_turn
    elif boardstate[0][1] == ai_opponent and boardstate[2][1] == ai_opponent and boardstate[1][1] == 0:
    	boardstate[1][1] = ai_turn
    elif boardstate[0][1] == ai_opponent and boardstate[1][1] == ai_opponent and boardstate[2][1] == 0:
    	boardstate[2][1] = ai_turn

    elif boardstate[1][2] == ai_opponent and boardstate[2][2] == ai_opponent and boardstate[0][2] == 0:
    	boardstate[0][2] = ai_turn
    elif boardstate[0][2] == ai_opponent and boardstate[2][2] == ai_opponent and boardstate[1][2] == 0:
    	boardstate[1][2] = ai_turn
    elif boardstate[0][2] == ai_opponent and boardstate[1][2] == ai_opponent and boardstate[2][2] == 0:
    	boardstate[2][2] = ai_turn

    elif boardstate[0][0] == ai_opponent and boardstate[1][1] == ai_opponent and boardstate[2][2] == 0:
    	boardstate[2][2] = ai_turn
    elif boardstate[1][1] == ai_opponent and boardstate[2][2] == ai_opponent and boardstate[0][0] == 0:
    	boardstate[0][0] = ai_turn
    elif boardstate[0][0] == ai_opponent and boardstate[2][2] == ai_opponent and boardstate[1][1] == 0:
    	boardstate[1][1] = ai_turn

    elif boardstate[0][2] == ai_opponent and boardstate[1][1] == ai_opponent and boardstate[2][0] == 0:
    	boardstate[2][0] = ai_turn
    elif boardstate[1][1] == ai_opponent and boardstate[2][0] == ai_opponent and boardstate[0][2] == 0:
    	boardstate[0][2] = ai_turn
    elif boardstate[0][2] == ai_opponent and boardstate[2][0] == ai_opponent and boardstate[1][1] == 0:
    	boardstate[1][1] = ai_turn

    else:
        turn_made = False
        for x in range(3):
            for y in range(3):
                if boardstate[y][x] == 0:
                    boardstate[y][x] = ai_turn
                    turn_made = True
                    break
            if turn_made:
                break
    return boardstate

    

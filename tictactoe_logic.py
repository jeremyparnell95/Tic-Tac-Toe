#tictactoe

class tictactoe:
    def __init__(self,turn):
        self._rows = 3
        self._columns = 3
        self._turn = turn
        self._winner = 0
        self._board = []

    def turn(self):
        return self._turn

    def change_turn(self):
        if self._turn == 1:
            self._turn = 2
        elif self._turn == 2:
            self._turn = 1
            
    def new_board(self):
        for col in range(self._columns):
            self._board.append([])
            for row in range(self._rows):
                self._board[-1].append(0)

    def print_board(self):
        for x in range(self._columns):
            content = ''
            for y in range(self._rows):
                if self._board[y][x] == 0:
                    content += "." + "  "
                elif self._board[y][x] == 1:
                    content += "X" + "  "
                elif self._board[y][x] == 2:
                    content += "O" + "  "   
            print(content)

    def move(self,row,column):
        if self.valid_move(row,column):
            self.check_diagonal()
            self.check_horizontal(row)
            self.check_vertical(column)
        else:
            raise Exception
        
    def winner(self):
        if self._winner > 0:
            return self._turn
        else:
            pass

    def check_diagonal(self):
        if self._board[1][1] != 0:
            if self._board[0][0] == self._board[1][1] and self._board[1][1] == self._board[2][2]:
                self._winner += 1
            if self._board[0][2] == self._board[1][1] and self._board[1][1] == self._board[2][0]:
                self._winner += 1
                   
    def check_horizontal(self,row):
        if self._board[1][row-1] != 0:
            if self._board[0][row-1] == self._board[1][row-1] and self._board[1][row-1] == self._board[2][row-1]:
                self._winner += 1

    def check_vertical(self,column):
        if self._board[column-1][1] != 0:
            if self._board[column-1][0] == self._board[column-1][1] and self._board[column-1][1] == self._board[column-1][2]:
                self._winner += 1
       
    def valid_move(self,row,column):
        if self._board[column-1][row-1] == 0:
            self._board[column-1][row-1] = self._turn
            return True
        else:
            return False

    def check_board(self):
        z = 0
        for x in range(3):
            for y in range(3):
                if self._board[x][y] > 0:
                    z += 1
                    if z == 9:
                        self._winner += 1
                        self._turn = 3
                    
                        
                
                

                        
                    


        
        
    
    
        
            
        

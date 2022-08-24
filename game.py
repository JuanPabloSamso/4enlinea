class inLine:
    def __init__(self):
        self.board = [[0 for _ in range(8)]for _ in range(8)]
        self.player = 1

    def available(self, col):
        for row in range(7,0,-1):
            if self.board [row][col] == 0:
                return row

    def throw_coin(self,col):
        self.board[self.available(col)][col] = self.player
        self.turn()

    def turn(self):
        if self.player == 1:
            self.player +=1
        else:
            self.player -= 1
            
    #def check_col(self):
        

    #def check_row(self):
         

    #def check_diag_up(self):
        

    #def check_diag_down(self):
        
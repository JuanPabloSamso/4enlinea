class inLine:
    def __init__(self):
        self.board = [[0 for _ in range(7)]for _ in range(6)]
        self.player = 1
        self.coin = ''

    def available(self, col):
        for row in range(6,0,-1):
            if self.board [row][col] == 0:
                return row

    def throw_coin(self,col):
        self.board[self.available(col)] = self.player
        self.turn()

    def turn(self):
        if self.player == 1:
            self.player +=1
        else:
            self.player -= 1

    def check_col(self):
        for c in range(7):
            for r in range(6-3):
                if self.board[r][c] == self.player and self.board[r+1][c] == self.player and self.board[r+2][c] == self.player and self.board[r+3][c] == self.player:
                    return True
         

    def check_row(self):
        for r in range(6):
            for c in range(7 - 3):
                if self.board[r][c] == self.player and self.board[r][c+1] == self.player and self.board[r][c+2] == self.player and self.board[r][c+3] == self.player:
                    return True
         
    def check_diag_down(self):
        for r in range(6):
            for c in range(7 - 3):
                if self.board[r][c] == self.player and self.board[r+1][c+1] == self.player and self.board[r+2][c+2] == self.player and self.board[r+3][c+3] == self.player:
                    return True


    #def check_diag_down(self):

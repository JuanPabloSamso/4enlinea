import unittest
from game import inLine

class TestInLine(unittest.TestCase):
    def test_board(self):
        game = inLine()
        self.assertEqual(len(game.board), 6)
        self.assertEqual(len(game.board[0]), 7)

    def test_available(self):
        game = inLine()
        game.available(1)
        self.assertEqual(game.available(0),7)

    def test_throw_coin(self):
        game = inLine()
        game.throw_coin(0)
        self.assertEqual(game.board[7][0],1)

    def test_turn1(self):
        game = inLine()
        game.turn()
        self.assertEqual(game.player,2)

    def test_turn2(self):
        game = inLine()
        game.player =2
        game.turn()
        self.assertEqual(game.player,1)

    def test_turn_after_play(self):
        game = inLine()
        game.throw_coin(0)
        self.assertEqual(game.player,2)

    def test_check_col_empty(self):
        game = inLine()
        game.check_col()
        game.board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]] 
        self.assertEqual(game.check_col(),None)

    def test_check_col_win(self):
        game = inLine()
        game.check_col()
        game.board = [[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.assertEqual(game.check_col(),True)

#    def test_check_row_empty(self):
 #       game = inLine()
  #      game.check_row()
   #     game.board([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
    #    ,[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
     #   self.assertEqual(game.check_row(),False)

#    def test_check_row_win(self):
 #       game = inLine()
  #      game.check_row()
   #     game.board([[1,1,1,1,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
    #    ,[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
     #   self.assertEqual(game.check_row(),True)

#    def test_check_diag_up_empty(self):
 #       game = inLine()
  #      game.check_diag_up()
   #     game.board([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
    #    ,[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
     #   self.assertEqual(game.check_row(),False)
    
#    def test_check_diag_up_win(self):
 #       game = inLine()
  #      game.check_diag_up()
   #     game.board([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0]
    #    ,[0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
     #   self.assertEqual(game.check_row(),True)

#    def test_check_diag_down_empty(self):
 #       game = inLine()
  #      game.check_diag_down()
   #     game.board([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]
    #    ,[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
     #   self.assertEqual(game.check_row(),False)
        
    def test_check_diag_down_win(self):
        game = inLine()
        game.check_diag_down()
        game.board = [[1,0,0,0,0,0,0,],[0,1,0,0,0,0,0,],[0,0,1,0,0,0,0,],[0,0,0,1,0,0,0,],[0,0,0,0,0,0,0,],[0,0,0,0,0,0,0,]]
        self.assertEqual(game.check_diag_down(),True)



if __name__ == '__main__':
    unittest.main() 

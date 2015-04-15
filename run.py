__author__ = 'Joshua'

from game import Game

game = Game()
game.run_game()
print game.get_pieces(1)
print game.get_moves(1, (2, 3))

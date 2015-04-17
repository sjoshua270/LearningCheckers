__author__ = 'Joshua'

from game import Game
from bot import Bot

game = Game()
player1 = Bot(1, game)
player2 = Bot(2, game)
while not game.finished():
    player1.make_move()
    player2.make_move()
    game.print_board()
__author__ = 'Joshua'

from game import Game
from bot import Bot

player1 = Bot(1)
player2 = Bot(2)

game = Game()
game.print_board()
while not game.finished():
    player1.make_move()
    player2.make_move()
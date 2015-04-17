__author__ = 'Joshua'

from time import sleep

from game import Game
from bot import Bot


game = Game()
player1 = Bot(1, game)
player2 = Bot(2, game)
turns = 0
while not game.finished():
    turns += 1
    player1.make_move()
    game.print_board()
    sleep(0.5)
    player2.make_move()
    game.print_board()
    sleep(0.5)
__author__ = 'Joshua'

from game import Game
from bot import Bot


game = Game()
player1 = Bot(1, game)
player2 = Bot(2, game)
turns = 0
while not game.finished():
    turns += 1
    player1.random_move()
    game.print_board()
    try:
        input()
    except:
        pass
    player2.random_move()
    game.print_board()
    try:
        input()
    except:
        pass
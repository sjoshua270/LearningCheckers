__author__ = 'Joshua'

from board import Board
from bot import Bot
from agent import Agent


board = Board()
agent1 = Agent(board, 1)
agent2 = Agent(board, 2)
player1 = Bot(board, agent1)
player2 = Bot(board, agent2)
all_turns = []
for x in range(0, 10):
    turns = 0
    while not board.finished():
        turns += 1
        player1.move()
        player2.move()
    board.print_board()
    all_turns.append(turns)
    board = Board()
print(all_turns)
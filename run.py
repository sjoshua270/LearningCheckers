__author__ = 'Joshua'

from board import Board
from bot import Bot
from agent import Agent


board = Board()
agent1 = Agent(board, 1, 0.1, 0.0, 0.5)
agent2 = Agent(board, 2, 0.8, 0.2, 0.9)
all_turns = []
for x in range(0, 1000):
    turns = 0
    finished = False
    player1 = Bot(board, agent1)
    player2 = Bot(board, agent2)
    message = "Win!"
    while not finished:
        turns += 1
        player1.move()
        player2.move()
        finished = board.finished()
        if turns > 400:
            finished = True
            message = "Stalemate"
    # print message
    b, r, bk, rk = board.get_values()
    # print("R: " + str(r) + " RK: " + str(rk) + " B: " + str(b) + " BK: " + str(bk))
    all_turns.append(turns)
    board = Board()
    agent1.set_board(board)
    agent2.set_board(board)
    if x % 100 == 99:
        print(sum(all_turns)/len(all_turns))
        all_turns = []
print(all_turns)
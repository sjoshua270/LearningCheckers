__author__ = 'Joshua'

import random


class Bot():
    def __init__(self, board, agent):
        self.board = board
        self.agent = agent

    def change_board(self, board):
        self.board = board

    def random_move(self):
        pieces = self.board.get_pieces(self.agent.number)
        moves = []
        for piece in pieces:
            directions = self.board.get_moves(self.agent.number, piece)
            for direction in directions:
                moves.append(direction)
        if len(moves) > 0:
            move = random.choice(moves)
            self.board.move_piece(self.agent.number, move, True)

    def move(self):
        move = self.agent.get_move(self.board)
        if move:
            self.board.move_piece(self.agent.number, move, True)
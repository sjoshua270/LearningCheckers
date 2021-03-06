__author__ = 'Joshua'

import random


class Agent():
    def __init__(self, board, number, alpha, epsilon, discount):
        self.alpha = alpha
        self.epsilon = epsilon
        self.discount = discount
        self.q_values = {}
        self.board = board
        self.number = number

    def set_board(self, board):
        self.board = board

    def get_q_value(self, board, move):
        key = str((board, move))
        try:
            return self.q_values[key]
        except KeyError:
            return 0.0

    def compute_value_from_q_value(self, board):
        max_q = float('-inf')
        for piece in self.board.get_pieces(self.number):
            for move in self.board.get_moves(self.number, piece):
                q = self.get_q_value(board, move)
                if q > max_q:
                    max_q = q
        if max_q == float('-inf'):
            return 0.0
        return max_q

    def compute_move_from_q_values(self, board):
        best_move = float('-inf')
        best_q = float('-inf')
        moves = []
        jump_moves = []
        for piece in self.board.get_pieces(self.number):
            for move in self.board.get_moves(self.number, piece):
                moves.append(move)
                if move[2]:
                    jump_moves.append(move)
        if len(jump_moves) > 0:
            moves = jump_moves

        for move in moves:
            q = self.get_q_value(board, move)
            if q > best_q:
                best_q = q
                best_move = move
        if best_q == float('-inf'):
            return None
        return best_move

    def get_move(self, board):
        moves = []
        jump_moves = []
        for piece in self.board.get_pieces(self.number):
            for move in self.board.get_moves(self.number, piece):
                moves.append(move)
        for move in moves:
            if move[2]:
                jump_moves.append(move)
        if random.randrange(0, 1) > self.epsilon:
            if len(jump_moves) > 0:
                return random.choice(jump_moves)
            return random.choice(moves)
        return self.compute_move_from_q_values(board)

    def update(self, board, move, next_board, reward):
        key = str((board, move))
        try:
            q = self.q_values[key]
        except KeyError:
            q = 0.0
        self.q_values[key] = (1 - self.alpha) * q + self.alpha * (
            reward + self.discount * self.compute_value_from_q_value(next_board))
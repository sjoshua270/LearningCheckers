__author__ = 'Joshua'

from game import Game


class Bot():
    def __init__(self, player_number):
        self.number = player_number
        self.game = Game()
        self.q_states = []

    def make_move(self):
        self.game
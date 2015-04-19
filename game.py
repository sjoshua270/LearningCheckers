__author__ = 'Joshua'

import copy
import sys


class Game():
    board_values = []
    reward = 10

    def __init__(self):
        self.board_values = [[0, 1, 0, 1, 0, 1, 0, 1],
                             [1, 0, 1, 0, 1, 0, 1, 0],
                             [0, 1, 0, 1, 0, 1, 0, 1],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [2, 0, 2, 0, 2, 0, 2, 0],
                             [0, 2, 0, 2, 0, 2, 0, 2],
                             [2, 0, 2, 0, 2, 0, 2, 0]]

    # player is the player's number
    def get_pieces(self, player):
        numbers = ()
        if player == 1:
            numbers = (1, 3)
        if player == 2:
            numbers = (2, 4)
        pieces = []
        for y in range(0, len(self.board_values)):
            for x in range(0, len(self.board_values[y])):
                board_number = self.board_values[y][x]
                if board_number in numbers:
                    pieces.append((y, x, board_number))
        return pieces

    # piece is a tuple (y, x, number)
    def get_directions(self, player, piece):
        moves = []
        y = piece[0]
        x = piece[1]
        number = piece[2]
        valid_pieces_down = (1, 3, 4)
        valid_pieces_up = (2, 3, 4)

        attack_targets = ()
        if player == 1:
            attack_targets = (2, 4)
        if player == 2:
            attack_targets = (1, 3)

        if number in valid_pieces_down:
            try:
                # DownRight
                new_space = self.board_values[y + 1][x + 1]
                if new_space == 0:
                    moves.append("DR")
                if new_space in attack_targets:
                    if self.board_values[y + 2][x + 2] == 0:
                        moves.append("DR")
            except IndexError:
                pass
            try:
                # DownLeft
                new_space = self.board_values[y + 1][x - 1]
                if new_space == 0 and not x - 1 < 0:
                    moves.append("DL")
                if new_space in attack_targets:
                    if self.board_values[y + 2][x - 2] == 0 and not x - 2 < 0:
                        moves.append("DL")
            except IndexError:
                pass

        if number in valid_pieces_up:
            try:
                # UpRight
                new_space = self.board_values[y - 1][x + 1]
                if new_space == 0 and not y - 1 < 0:
                    moves.append("UR")
                if new_space in attack_targets:
                    if self.board_values[y - 2][x + 2] == 0 and not y - 2 < 0:
                        moves.append("UR")
            except IndexError:
                pass
            try:
                # UpLeft
                new_space = self.board_values[y - 1][x - 1]
                if new_space == 0 and not (y - 1 < 0 or x - 1 < 0):
                    moves.append("UL")
                if new_space in attack_targets:
                    if self.board_values[y - 2][x - 2] == 0 and not (y - 2 < 0 or x - 2 < 0):
                        moves.append("UL")
            except IndexError:
                pass

        return moves

    # move corresponds of (piece, direction)
    # confirm is whether or not to submit the move
    def move_piece(self, player, move, confirm):
        y = move[0][0]
        x = move[0][1]
        number = move[0][2]
        direction = move[1]
        board = copy.deepcopy(self.board_values)
        reward = 0
        valid_players_down = (1, 3, 4)
        valid_players_up = (2, 3, 4)

        if number in valid_players_down:
            if direction == "DR":
                new_space = board[y + 1][x + 1]
                if new_space == 0:
                    board[y][x] = 0
                    board[y + 1][x + 1] = number
                if new_space == 2:
                    board[y][x] = 0
                    board[y + 1][x + 1] = 0
                    board[y + 2][x + 2] = number
                    reward = self.reward

            if direction == "DL":
                new_space = board[y + 1][x - 1]
                if new_space == 0:
                    board[y][x] = 0
                    board[y + 1][x - 1] = number
                if new_space == 2:
                    board[y][x] = 0
                    board[y + 1][x - 1] = 0
                    board[y + 2][x - 2] = number
                    reward = self.reward

        if number in valid_players_up:
            if direction == "UR":
                new_space = board[y - 1][x + 1]
                if new_space == 0:
                    board[y][x] = 0
                    board[y - 1][x + 1] = number
                if new_space == 1:
                    board[y][x] = 0
                    board[y - 1][x + 1] = 0
                    board[y - 2][x + 2] = number
                    reward = self.reward

            if direction == "UL":
                new_space = board[y - 1][x - 1]
                if new_space == 0:
                    board[y][x] = 0
                    board[y - 1][x - 1] = number
                if new_space == 1:
                    board[y][x] = 0
                    board[y - 1][x - 1] = 0
                    board[y - 2][x - 2] = number
                    reward = self.reward
        if confirm:
            self.board_values = board
        if self.king_achieved(player, confirm):
            reward = 50
        return board, reward

    def king_achieved(self, player, confirm):
        king = False
        if player == 1:
            y = 7
        if player == 2:
            y = 0
        for x in range(0, 8):
            if self.board_values[y][x] == player:
                king = True
                if confirm:
                    self.board_values[y][x] = player + 2
        return king

    def print_board(self):
        print_values = {
            0: '|   ',
            1: '| B ',
            2: '| R ',
            3: '| BK',
            4: '| RK'
        }
        output = "YX  0   1   2   3   4   5   6   7\n"
        output += "  ,-------------------------------,\n"
        for y in range(0, len(self.board_values)):
            line = str(y) + " "
            divider = "  "
            for x in range(0, len(self.board_values[y])):
                line += print_values[self.board_values[y][x]]
                divider += "|---"
            output += (line + "|\n")
            if y != len(self.board_values) - 1:
                output += (divider + "|\n")
        output += "  '-------------------------------'\n"
        sys.stdout.write(output)
        for row in self.board_values:
            sys.stdout.write(str(row) + "\n")

    def finished(self):
        p1_count = 0
        p2_count = 0
        for y in range(0, len(self.board_values)):
            for x in range(0, len(self.board_values[y])):
                piece_number = self.board_values[y][x]
                if piece_number == 1 or piece_number == 3:
                    p1_count += 1
                if piece_number == 2 or piece_number == 4:
                    p2_count += 1

        if p1_count == 0 or p2_count == 0:
            return True
        else:
            return False
__author__ = 'Joshua'

import copy
import sys


class Board():
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

    def get_moves(self, player, piece):
        valid_moves = []
        y = piece[0]
        x = piece[1]
        number = piece[2]
        diffs = {}
        valid_targets = ()
        directions = ()

        if player == 1:
            valid_targets = (0, 2, 4)
            if number == 1:
                directions = ("DR", "DL")
                diffs = {'y': (1, 1), 'x': (1, -1)}
            if number == 3:
                directions = ("UR", "UL", "DR", "DL")
                diffs = {'y': (-1, -1, 1, 1), 'x': (1, -1, 1, -1)}

        if player == 2:
            valid_targets = (0, 1, 3)
            if number == 2:
                directions = ("UR", "UL")
                diffs = {'y': (-1, -1), 'x': (1, -1)}
            if number == 4:
                directions = ("UR", "UL", "DR", "DL")
                diffs = {'y': (-1, -1, 1, 1), 'x': (1, -1, 1, -1)}

        for i in range(0, len(diffs['y'])):
            new_y = y + diffs['y'][i]
            new_x = x + diffs['x'][i]

            # Make sure we are in the board range
            if 0 <= new_y < 8 and 0 <= new_x < 8:
                new_space = self.board_values[new_y][new_x]
                if new_space in valid_targets:
                    # If new space is empty
                    if new_space == valid_targets[0]:
                        valid_moves.append((piece, directions[i], False))
                    # If we can jump
                    else:
                        new_y += diffs['y'][i]
                        new_x += diffs['x'][i]
                        # Will pass if index out of range
                        try:
                            new_space = self.board_values[new_y][new_x]
                            if new_space == 0:
                                valid_moves.append((piece, directions[i], True))
                        except IndexError:
                            pass

        return valid_moves

    # Arg 'move' is comprised of (piece(y, x, number), direction(str), jump(bool))
    # Confirm is whether or not to apply the attempted move
    def move_piece(self, player, move, confirm):
        y = move[0][0]
        x = move[0][1]
        number = move[0][2]
        direction = move[1]
        jump = move[2]
        board = copy.deepcopy(self.board_values)
        reward = 0
        moves_diff = {
            "DR": (1, 1),
            "DL": (1, -1),
            "UR": (-1, 1),
            "UL": (-1, -1)
        }

        new_y = y + moves_diff[direction][0]
        new_x = x + moves_diff[direction][1]
        if jump:
            board[new_y][new_x] = 0
            new_y += moves_diff[direction][0]
            new_x += moves_diff[direction][1]
            reward = 10

        board[y][x] = 0
        board[new_y][new_x] = number

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

    def get_values(self):
        p1_count = 0
        p2_count = 0
        p1_kount = 0
        p2_kount = 0
        for y in range(0, len(self.board_values)):
            for x in range(0, len(self.board_values[y])):
                if self.board_values[y][x] == 1:
                    p1_count += 1
                if self.board_values[y][x] == 2:
                    p2_count += 1
                if self.board_values[y][x] == 3:
                    p1_kount += 1
                if self.board_values[y][x] == 4:
                    p2_kount += 1
        return p1_count, p2_count, p1_kount, p2_kount

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
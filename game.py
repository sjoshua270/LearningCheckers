__author__ = 'Joshua'

import copy

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
        pieces = []
        for y in range(0, len(self.board_values)):
            for x in range(0, len(self.board_values[y])):
                if self.board_values[y][x] == player:
                    pieces.append((y, x))
        return pieces

    # piece is a tuple (y, x)
    def get_moves(self, player, piece):
        moves = []
        y = piece[0]
        x = piece[1]
        if player == 1 or player == 3 or player == 4:
            try:
                # DownRight
                new_space = self.board_values[y + 1][x + 1]
                if new_space == 0:

                    moves.append("DR")
                if new_space == 2:
                    if self.board_values[y + 2][x + 2] == 0:
                        moves.append("DR")
            except IndexError:
                pass
            try:
                # DownLeft
                new_space = self.board_values[y + 1][x - 1]
                if new_space == 0 and not x - 1 < 0:
                    moves.append("DL")
                if new_space == 2:
                    if self.board_values[y + 2][x - 2] == 0 and not x - 2 < 0:
                        moves.append("DL")
            except IndexError:
                pass

        if player == 2 or player == 3 or player == 4:
            try:
                # UpRight
                new_space = self.board_values[y - 1][x + 1]
                if new_space == 0 and not y - 1 < 0:
                    moves.append("UR")
                if new_space == 1:
                    if self.board_values[y - 2][x + 2] == 0 and not y - 2 < 0:
                        moves.append("UR")
            except IndexError:
                pass
            try:
                # UpLeft
                new_space = self.board_values[y - 1][x - 1]
                if new_space == 0 and not (y - 1 < 0 or x - 1 < 0):
                    moves.append("UL")
                if new_space == 1:
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
        direction = move[1]
        board = copy.deepcopy(self.board_values)
        reward = 0

        if player == 1 or player == 3 or player == 4:
            if direction == "DR":
                new_space = board[y + 1][x + 1]
                if new_space == 0:
                    board[y][x] = 0
                    board[y + 1][x + 1] = player
                if new_space == 2:
                    board[y][x] = 0
                    board[y + 1][x + 1] = 0
                    board[y + 2][x + 2] = player
                    reward = self.reward

            if direction == "DL":
                new_space = board[y + 1][x - 1]
                if new_space == 0:
                    board[y][x] = 0
                    board[y + 1][x - 1] = player
                if new_space == 2:
                    board[y][x] = 0
                    board[y + 1][x - 1] = 0
                    board[y + 2][x - 2] = player
                    reward = self.reward

        if player == 2:
            if direction == "UR":
                new_space = board[y - 1][x + 1]
                if new_space == 0:
                    board[y][x] = 0
                    board[y - 1][x + 1] = player
                if new_space == 1:
                    board[y][x] = 0
                    board[y - 1][x + 1] = 0
                    board[y - 2][x + 2] = player
                    reward = self.reward

            if direction == "UL":
                new_space = board[y - 1][x - 1]
                if new_space == 0:
                    board[y][x] = 0
                    board[y - 1][x - 1] = player
                if new_space == 1:
                    board[y][x] = 0
                    board[y - 1][x - 1] = 0
                    board[y - 2][x - 2] = player
                    reward = self.reward
        if confirm:
            self.board_values = board
        return board, reward

    def print_board(self):
        print_values = {
            0: '|   ',
            1: '| B ',
            2: '| R ',
            3: '| BK',
            4: '| RK'
        }
        print("YX  0   1   2   3   4   5   6   7")
        print("  ,-------------------------------,")
        for y in range(0, len(self.board_values)):
            line = str(y) + " "
            divider = "  "
            for x in range(0, len(self.board_values[y])):
                line += print_values[self.board_values[y][x]]
                divider += "|---"
            print(line + "|")
            if y != len(self.board_values) - 1:
                print(divider + "|")
        print("  '-------------------------------'")

    def finished(self):
        p1_count = 0
        p2_count = 0
        for y in range(0, len(self.board_values)):
            for x in range(0, len(self.board_values[y])):
                if self.board_values[y][x] == 1:
                    p1_count += 1
                if self.board_values[y][x] == 2:
                    p2_count += 1

        if p1_count == 0 or p2_count == 0:
            return True
        else:
            return False
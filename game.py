__author__ = 'Joshua'


class Game():
    checker_board_dimensions = 0
    board_values = []

    def __init__(self):
        global checker_board_dimensions
        global board_values
        checker_board_dimensions = (8, 8)
        board_values = [[0, 1, 0, 1, 0, 1, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0],
                        [0, 1, 0, 1, 0, 1, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [2, 0, 2, 0, 2, 0, 2, 0],
                        [0, 2, 0, 2, 0, 2, 0, 2],
                        [2, 0, 2, 0, 2, 0, 2, 0]]

    def run_game(self):
        self.print_board()

    # piece is a tuple (x, y)
    def move_piece(self, player, piece, direction):
        global board_values
        x = piece[0]
        y = piece[1]
        if direction == "UR":
            if board_values[x + 1][y - 1] == 0:
                board_values[x][y] = 0
                board_values[x + 1][y - 1] = player

        if direction == "UL":
            if board_values[x - 1][y - 1] == 0:
                board_values[x][y] = 0
                board_values[x - 1][y - 1] = player

        if direction == "DR":
            if board_values[x + 1][y + 1] == 0:
                board_values[x][y] = 0
                board_values[x + 1][y + 1] = player

        if direction == "DL":
            if board_values[x - 1][y + 1] == 0:
                board_values[x][y] = 0
                board_values[x - 1][y + 1] = player


    # player is the player's number
    def get_pieces(self, player):
        global board_values
        pieces = []
        for x in range(0, len(board_values)):
            for y in range(0, len(board_values[x])):
                if board_values[x][y] == player:
                    pieces.append((x, y))
        return pieces

    # piece is a tuple (x, y)
    def get_moves(self, player, piece):
        global board_values
        moves = []
        x = piece[0]
        y = piece[1]

        if player == 1:
            try:
                # DR
                if board_values[x + 1][y + 1] == 0:
                    moves.append("DR")
            except IndexError:
                pass
            try:
                # DL
                if board_values[x + 1][y - 1] == 0:
                    moves.append("DL")
            except IndexError:
                pass

        if player == 2:
            try:
                # UR
                if board_values[x - 1][y + 1] == 0:
                    moves.append("UR")
            except IndexError:
                pass
            try:
                # UL
                if board_values[x - 1][y - 1] == 0:
                    moves.append("UL")
            except IndexError:
                pass

        return moves

    @staticmethod
    def print_board():
        global board_values
        global checker_board_dimensions
        for x in range(0, checker_board_dimensions[0]):
            line = ""
            for y in range(0, checker_board_dimensions[1]):
                if board_values[x][y] == 1:
                    line += "| B "
                elif board_values[x][y] == 2:
                    line += "| R "
                else:
                    line += "|   "
            line += "|"
            print(line)
            print("---------------------------------")

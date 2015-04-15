__author__ = 'Joshua'


class Game():
    board_values = []

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

        if player == 1:
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
                if new_space == 0:
                    moves.append("DL")
                if new_space == 2:
                    if self.board_values[y + 2][x - 2]:
                        moves.append("DL")
            except IndexError:
                pass

        if player == 2:
            try:
                # UpRight
                new_space = self.board_values[y - 1][x + 1]
                if new_space == 0:
                    moves.append("UR")
                if new_space == 1:
                    if self.board_values[y - 2][x + 2]:
                        moves.append("UR")
            except IndexError:
                pass
            try:
                # UpLeft
                new_space = self.board_values[y - 1][x - 1]
                if new_space == 0:
                    moves.append("UL")
                if new_space == 1:
                    if self.board_values[y - 2][x - 2]:
                        moves.append("UL")
            except IndexError:
                pass

        return moves

    # piece is a tuple (x, y)

    def move_piece(self, player, piece, direction):
        y = piece[0]
        x = piece[1]

        if player == 1:
            if direction == "DR":
                new_space = self.board_values[y + 1][x + 1]
                if new_space == 0:
                    self.board_values[y][x] = 0
                    self.board_values[y + 1][x + 1] = player
                    return 0
                if new_space == 2:
                    self.board_values[y][x] = 0
                    self.board_values[y + 1][x + 1] = 0
                    self.board_values[y + 2][x + 2] = player
                    return 10

            if direction == "DL":
                new_space = self.board_values[y + 1][x - 1]
                if new_space == 0:
                    self.board_values[y][x] = 0
                    self.board_values[y + 1][x - 1] = player
                    return 0
                if new_space == 2:
                    self.board_values[y][x] = 0
                    self.board_values[y + 1][x - 1] = 0
                    self.board_values[y + 2][x - 2] = player
                    return 10

        if player == 2:
            if direction == "UR":
                new_space = self.board_values[y - 1][x + 1]
                if new_space == 0:
                    self.board_values[y][x] = 0
                    self.board_values[y - 1][x + 1] = player
                    return 0
                if new_space == 1:
                    self.board_values[y][x] = 0
                    self.board_values[y - 1][x + 1] = 0
                    self.board_values[y - 2][x + 2] = player
                    return 10

            if direction == "UL":
                new_space = self.board_values[y - 1][x - 1]
                if new_space == 0:
                    self.board_values[y][x] = 0
                    self.board_values[y - 1][x - 1] = player
                if new_space == 1:
                    self.board_values[y][x] = 0
                    self.board_values[y - 1][x - 1] = 0
                    self.board_values[y - 2][x - 2] = player
                    return 10

    def print_board(self):
        print("YX  0   1   2   3   4   5   6   7")
        print("  ,-------------------------------,")
        for y in range(0, len(self.board_values)):
            line = str(y) + " "
            divider = "  "
            for x in range(0, len(self.board_values[y])):
                if self.board_values[y][x] == 4:
                    line += "| T "
                if self.board_values[y][x] == 1:
                    line += "| B "
                elif self.board_values[y][x] == 2:
                    line += "| R "
                else:
                    line += "|   "
                divider += "|---"
            print(line + "|")
            if y != len(self.board_values) - 1:
                print(divider + "|")
        print("  '-------------------------------'")

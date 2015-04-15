__author__ = 'Joshua'


class Game():
    checker_board_dimensions = 0
    board_values = 0
    def __init__(self):
        global checker_board_dimensions
        global board_values
        checker_board_dimensions = (8, 8)
        board_values = ((0, 1, 0, 1, 0, 1, 0, 1),
                        (1, 0, 1, 0, 1, 0, 1, 0),
                        (0, 1, 0, 1, 0, 1, 0, 1),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (2, 0, 2, 0, 2, 0, 2, 0),
                        (0, 2, 0, 2, 0, 2, 0, 2),
                        (2, 0, 2, 0, 2, 0, 2, 0))

    @staticmethod
    def run_game():
        global checker_board_dimensions
        for x in range(0, checker_board_dimensions[0]):
            line = ""
            for y in range(0, checker_board_dimensions[1]):
                line += "|  "
            line += "|"
            print(line)
            print("-------------------------")
    def print_board(self):
        global board_values
        checker_board_dimensions = (8, 8)
        for x in range(0, checker_board_dimensions[0]):
            line = ""
            for y in range(0, checker_board_dimensions[1]):
                line += "|  "
            line += "|"
            print(line)
            print("-------------------------")

__author__ = 'Joshua'


class Game():

    def __init__(self):
        pass

    def run_game(self):
        checker_board_dimensions = (8, 8)
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

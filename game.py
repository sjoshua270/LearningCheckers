__author__ = 'Joshua'


class LaunchGame():
    def __init__(self):
        checker_board_dimensions = (8, 8)
        line = ""
        for x in range(0, checker_board_dimensions[0]):
            for y in range(0, checker_board_dimensions[1]):
                line += "| "
            line += "|"
            print(line)
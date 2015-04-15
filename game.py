__author__ = 'Joshua'


class launch_game():
    def __init__(self):
        check_dimens = (8, 8)
        line = ""
        for x in range(0, check_dimens[0]):
            for y in range(0, check_dimens[1]):
                line += "| "
            line += "|"
            print(line)

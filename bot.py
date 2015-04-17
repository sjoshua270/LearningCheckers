__author__ = 'Joshua'


class Bot():
    def __init__(self, player_number, game):
        self.number = player_number
        self.game = game
        self.q_states = {}

    def basic_move(self):
        pieces = self.game.get_pieces(self.number)
        done = False
        move = ()
        for piece in pieces:
            if not done:
                directions = self.game.get_moves(self.number, piece)
                if len(directions) > 0:
                    done = True
                    move = (piece, directions[0])
        if not len(move) == 0:
            self.game.move_piece(self.number, move, True)

    def make_move(self):
        pieces = self.game.get_pieces(self.number)
        best_qvalue = float('-inf')
        best_move = None
        for piece in pieces:
            actions = self.game.get_moves(self.number, piece)
            for action in actions:
                move = (piece, action)
                # move_piece() returns tuple: (board, reward)
                new_board = self.game.move_piece(self.number, move, False)
                if new_board[1] > best_qvalue:
                    best_qvalue = new_board[1]
                    best_move = (piece, action)
        if best_move is not None:
            print("Player %s" % self.number)
            print(best_move)
            self.game.move_piece(self.number, best_move, True)
            self.update_qvalue(self.game.board_values, best_move)

    def update_qvalue(self, board, move):
        key = str((board, move))
        self.q_states[key] = self.game.move_piece(self.number, move, False)

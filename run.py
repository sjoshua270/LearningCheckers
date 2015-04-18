__author__ = 'Joshua'

from game import Game

player = 1

game = Game()
game.print_board()
for x in range(0, 10):
    pieces = game.get_pieces(player)
    moves = []
    iteration = -1
    while len(moves) == 0:
        iteration += 1
        moves = game.get_moves(player, pieces[iteration])
    print(pieces[iteration])
    print(moves)
    game.move_piece(player, pieces[iteration], moves[0])
    game.print_board()


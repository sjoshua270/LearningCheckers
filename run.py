__author__ = 'Joshua'

from game import Game

player = 1

game = Game()
game.run_game()
for x in range(0, 5):
    pieces = game.get_pieces(player)
    moves = []
    iteration = 0
    while len(moves) == 0:
        moves = game.get_moves(player, pieces[iteration])
        iteration += 1
    print(pieces[iteration])
    print(moves)
    game.move_piece(player, pieces[iteration], moves[0])
    game.print_board()



class Board:
    # Initialize the game field - list of lists with spaces.
    # Spaces are empty cells.
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    # Method that processes player moves.
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Method that draws the playing field.
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)


# Create game field - Board object.
game = Board()
# Draw the field in the terminal.
game.display()
# Place the symbol on the field according
# to the given coordinates - make a move.
game.make_move(1, 1, 'X')
print('The move has been made!')

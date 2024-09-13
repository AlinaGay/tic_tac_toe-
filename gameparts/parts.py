class Board:
    field_size = 3
    # Initialize the game field - list of lists with spaces.
    # Spaces are empty cells.
    def __init__(self):
        self.board = [[' ' for _ in range(self.field_size)] for _ in range(self.field_size)]

    # Method that processes player moves.
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Method that draws the playing field.
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def __str__(self):
        return (
            'Size of the game field object'
            f'{self.field_size}x{self.field_size}'
        )
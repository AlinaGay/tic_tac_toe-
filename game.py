from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOcupiederror


def main():
    # Create game field - Board object.
    game = Board()
    current_payer = 'X'
    running = True
    # Draw the field in the terminal.
    game.display()

    while running:
        print(f'Run by {current_payer}')

        while True:
            try:
                row = int(input('Enter the number of row: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Enter the number of column: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOcupiederror
            except FieldIndexError:
                print(
                    'Value must be non-negative and less than'
                    f'{game.field_size}.'
                )
                print('Please enter the values for the row and column again.')
                continue
            except CellOcupiederror:
                print('The cell is ocupied.')
                print('Enter the different coordinates.')
            except ValueError:
                print(
                    'You cannot enter letters. Only numbers.'
                )
                print('Please enter the values for the row and column again.')
                continue
            except Exception as e:
                print(f'There is error: {e}')
            else:
                break

        game.make_move(row, column, current_payer)
        game.display()

        if game.check_win(current_payer):
            print(f'Won {current_payer}')
            running = False
        elif game.is_board_full():
            print('A draw!')
            running = False

        current_payer = 'O' if current_payer == 'X' else 'X'


if __name__ == '__main__':
    main()

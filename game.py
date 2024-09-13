from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    # Create game field - Board object.
    game = Board()
    # Draw the field in the terminal.
    game.display()

    while True:
        try:
            row = int(input('Enter the number of row: '))

            if row < 0 or row >= game.field_size:
                raise FieldIndexError
            column = int(input('Enter the number of column: '))

            if column < 0 or column >= game.field_size:
                raise FieldIndexError

        except FieldIndexError:
            print(
                'Value must be non-negative and less than'
                f'{game.field_size}.'
            )
            print('Please enter the values for the row and column again.')
            continue
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
    game.make_move(row, column, 'X')
    print('The move has been made!')
    game.display()


if __name__ == '__main__':
    main()

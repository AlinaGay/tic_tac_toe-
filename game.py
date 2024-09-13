from gameparts import Board


def main():
    # Create game field - Board object.
    game = Board()
    # Draw the field in the terminal.
    game.display()
    # Place the symbol on the field according
    # to the given coordinates - make a move.
    game.make_move(1, 1, 'X')
    print('The move has been made!')
    game.display()


if __name__ == '__main__':
    main()

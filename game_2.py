import pygame

from gameparts import Board

pygame.init()

CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (20, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

# size of the graphic window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# set the name of window
pygame.display.set_caption('Tic-Tac Toe')
screen.fill(BG_COLOR)


def draw_lines():
    for i in range(1, BOARD_SIZE):
        # Horizontal lines
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )

        # Vertical lines
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )


# Function for drawing X and O on the board
def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )


def save_result(result):
    with open('results.txt', 'a') as file:
        file.write(result + '\n')


def main():
    # Create game field - Board object.
    game = Board()
    current_payer = 'X'
    running = True
    # Draw the field in the pygame window.
    draw_lines()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE

                if game.board[clicked_row][clicked_col] == ' ':
                    game.make_move(clicked_row, clicked_col, current_payer)
                if game.check_win(current_payer):
                    result = f'Won {current_payer}'
                    print(result)
                    save_result(result)
                    running = False
                elif game.is_board_full():
                    result = 'A draw!'
                    print(result)
                    save_result(result)
                    running = False

                current_payer = 'O' if current_payer == 'X' else 'X'
                draw_figures(game.board)

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()

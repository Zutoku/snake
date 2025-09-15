import curses
from game_board import GameBoard
from snake import Snake
from food import Food
from game_loop import Game


def main(stdscr):
    while True:
        stdscr.keypad(True)
        curses.echo()
        stdscr.nodelay(0)
        curses.curs_set(1)  # Show cursor for input
        stdscr.clear()
        stdscr.refresh()
        x = 0
        y = 0

        stdscr.addstr("Welcome to snake!\n")
        try:
            stdscr.addstr("Please select a game width: ")
            x = int(stdscr.getstr().decode("utf-8"))

            stdscr.addstr("Please select a game height: ")
            y = int(stdscr.getstr().decode("utf-8"))

        except ValueError:
            stdscr.addstr("Please only use integers\n")
            stdscr.addstr("Press enter to try again: ")
            stdscr.getstr()
            continue

        if not (0 < x <= 21 and 0 < y <= 21):
            stdscr.addstr("Please choose an integer between 0 and 21\n")
            stdscr.addstr("Press enter to try again: ")
            stdscr.getstr()
            continue

        stdscr.clear()
        game_board = GameBoard(y, x)
        snake = Snake(1, 1, game_board.game_height, game_board.game_width)
        food = Food(y, x)
        game_board.print_board(stdscr)

        # Prevent pressed keys from displaying in terminal
        curses.noecho()
        # This enables key presses to go through without needing enter
        # curses.cbreak()
        # This hides the cursor
        # Make getch() non-blocking
        stdscr.nodelay(1)

        curses.curs_set(False)
        game = Game()
        game.run(stdscr, game_board, snake, food)

    # key = stdscr.getstr()
    # if key == ord("q"):
    #     break
    # x = 1
    # y = 1
    # # game loop starts here:
    # start_time = time.time()
    # running = True
    # hard_mode = False
    # while running:
    #     time_elapsed = time.time() - start_time
    #     key = stdscr.getch()
    #     game_board.fill_board()
    #
    #     match key:
    #         case 113:  # ASCII code for letter q
    #             running = False
    #         case curses.KEY_UP:
    #             snake.direction = Direction.UP
    #         case curses.KEY_DOWN:
    #             snake.direction = Direction.DOWN
    #         case curses.KEY_LEFT:
    #             snake.direction = Direction.LEFT
    #         case curses.KEY_RIGHT:
    #             snake.direction = Direction.RIGHT
    #
    #     # if 0 < x < game_board.width and 0 < y < game_board.height:
    #     for y, x in snake.positions:
    #         game_board.set_value(y, x, snake.SNAKE_SHAPE)
    #         # game_board.board[(position)] = snake.SNAKE_SHAPE
    #
    #     if time_elapsed > 1.0:
    #         snake.update_direction()
    #         snake.update_snake()
    #
    #         if snake.is_out_of_bounds() and hard_mode:
    #             running = False
    #
    #         # y, x = snake.update_position()
    #         start_time = time.time()
    #
    #     stdscr.clear()
    #     game_board.print_board(stdscr)
    #     stdscr.addstr(f"{time_elapsed}\n")
    #     stdscr.addstr(f"{snake.positions}\n")
    #     stdscr.refresh()
    #     # Small delay to reduce CPU usage
    #     time.sleep(0.1)


if __name__ == "__main__":
    curses.wrapper(main)

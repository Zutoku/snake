import curses
from game_board import GameBoard
from snake import Snake
from food import Food
from game_loop import Game


def main(stdscr):
    while True:
        curses.start_color()
        # Define color pairs (foreground, background)
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        colour_green = curses.color_pair(1)
        colour_yellow = curses.color_pair(2)

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
        game = Game(colour_green, colour_yellow)
        game.run(stdscr, game_board, snake, food)
        stdscr.nodelay(0)
        stdscr.addstr("You lost! Press ENTER to try again: ")
        stdscr.getstr()


if __name__ == "__main__":
    curses.wrapper(main)

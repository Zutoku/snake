import time
import curses
from game_board import GameBoard


def main(stdscr):
    stdscr.keypad(True)
    curses.echo()

    stdscr.addstr("Welcome to snake!\n")
    while True:
        try:
            stdscr.addstr("Please select a game width: ")
            x = int(stdscr.getstr().decode("utf-8"))

            stdscr.addstr("Please select a game height: ")
            y = int(stdscr.getstr().decode("utf-8"))
        except ValueError:
            stdscr.addstr("Please only use integers\n")
            continue
        if 0 < x <= 21 and 0 < y <= 21:
            break
        stdscr.addstr("Please choose an integer between 0 and 21\n")

    stdscr.clear()
    game_board = GameBoard(y, x)
    game_board.board[1, 1] = "~"
    game_board.print_board(stdscr)

    # Prevent pressed keys from displaying in terminal
    curses.noecho()
    # This enables key presses to go through without needing enter
    # curses.cbreak()
    # This hides the cursor
    # Make getch() non-blocking
    stdscr.nodelay(1)

    curses.curs_set(False)
    x = 1
    y = 1
    start_time = time.time()
    # game loop starts here:
    while True:
        time_elapsed = time.time() - start_time
        key = stdscr.getch()
        game_board.fill_board()
        # Why not use else if?
        # Switch/match is faster,
        # look at how it's interpreted in assembly
        match key:
            case 113:  # ASCII code for letter q
                break
            case curses.KEY_UP:
                stdscr.clear()
                y -= 2
            case curses.KEY_DOWN:
                stdscr.clear()
                y += 2
            case curses.KEY_LEFT:
                stdscr.clear()
                x -= 2
            case curses.KEY_RIGHT:
                stdscr.clear()
                x += 2
        if 0 < x < game_board.width and 0 < y < game_board.height:
            game_board.board[y, x] = "~"
        if time_elapsed > 2.0:
            start_time = time.time()
        stdscr.clear()
        game_board.print_board(stdscr)
        stdscr.addstr(f"{time_elapsed}\n")
        stdscr.refresh()
        time.sleep(0.1)
    # Small delay to reduce CPU usage# Reset terminal to normal state
    # NOT NEEDED AS HANDLED BY WRAPPER
    # curses.nocbreak(), stdscr.keypad(False)
    # curses.echo()
    # curses.endwin()


if __name__ == "__main__":
    curses.wrapper(main)

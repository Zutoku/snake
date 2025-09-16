import curses
import numpy as np


class GameBoard:
    def __init__(self, game_height, game_width):
        self.game_width = game_width
        self.game_height = game_height
        self.height = 2 * game_width + 1
        self.width = 2 * game_height + 1
        self.VERTICAL_LINE = "|"
        self.HORIZONTAL_LINE = "-"
        self.CORNERS = "+"
        self.GRID_OFFSET = 2
        self.board = np.full((self.height, self.width), " ", dtype=object)
        self.fill_board()

    def print_board(self, stdscr):
        try:
            stdscr.addstr("  ")
            for index in range(1, self.game_width + 1):
                stdscr.addstr(f" {index}")
            stdscr.addstr("\n")
            for i in range(self.height):
                if i % 2 == 1:
                    stdscr.addstr(f"{(i // 2) + 1:>2}")
                else:
                    stdscr.addstr("  ")

                for j in range(self.width):
                    stdscr.addstr(f"{self.board[i][j]}")
                stdscr.addstr("\n")
        except curses.error:
            pass

    def fill_board(self):
        self.board = np.full((self.height, self.width), " ", dtype=object)
        # Top and bottom edge
        self.board[0, :] = self.board[self.height - 1, :] = self.HORIZONTAL_LINE
        # Left and Right edge
        self.board[:, 0] = self.board[:, self.width - 1] = self.VERTICAL_LINE
        # Corners
        self.board[0, 0] = self.board[self.height - 1, 0] = self.board[
            0, self.width - 1
        ] = self.board[self.height - 1, self.width - 1] = self.CORNERS

        for i in range(0, self.height, 2):
            self.board[i, :] = self.HORIZONTAL_LINE
            for j in range(0, self.width, 2):
                self.board[:, j] = self.VERTICAL_LINE

        for i in range(0, self.height, 2):
            for j in range(0, self.width, 2):
                self.board[i][j] = self.CORNERS

    def set_value(self, y, x, value):
        if x > 1:
            x = (x * self.GRID_OFFSET) - 1
        if y > 1:
            y = (y * self.GRID_OFFSET) - 1

        y = max(1, min(y, self.height - 1))
        x = max(1, min(x, self.width - 1))
        self.board[y, x] = value

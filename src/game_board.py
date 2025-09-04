import numpy as np


class GameBoard:
    def __init__(self, game_width, game_height):
        self.game_width = game_width
        self.game_height = game_height

        self.width = 2 * game_width + 1
        self.height = 2 * game_height + 1

        self.VERTICAL_LINE = "|"
        self.HORIZONTAL_LINE = "-"
        self.CORNERS = "+"

        self.board = np.full((self.width, self.height), " ", dtype=object)
        self.fill_board()

    def print_board(self):
        for i in range(self.width):
            for j in range(self.height):
                print(self.board[i][j], end="")
            print()

    def fill_board(self):
        # Top and bottom edge
        self.board[0, :] = self.board[self.width - 1, :] = self.HORIZONTAL_LINE
        # Left and Right edge
        self.board[:, 0] = self.board[:, self.height - 1] = self.VERTICAL_LINE
        # Corners
        self.board[0, 0] = self.board[self.width - 1, 0] = self.board[
            0, self.height - 1
        ] = self.board[self.width - 1, self.height - 1] = self.CORNERS

        for i in range(0, self.width, 2):
            self.board[i, :] = self.HORIZONTAL_LINE
            for j in range(0, self.height, 2):
                self.board[:, j] = self.VERTICAL_LINE

        for i in range(0, self.width, 2):
            for j in range(0, self.height, 2):
                self.board[i][j] = self.CORNERS

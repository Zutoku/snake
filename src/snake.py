from snake_element import SnakeElement
from constants import Direction
from typing import List, Tuple


class Snake:
    def __init__(self, y, x, board_height, board_width) -> None:
        self.GRID_OFFSET = 2
        self.SNAKE_SHAPE = "#"
        self.board_height = board_height
        self.board_width = board_width
        self.y = y
        self.x = x
        self.direction = Direction.DOWN
        self.snake_length = 5
        self.positions: List[Tuple] = [(0, 0) for _ in range(self.snake_length + 1)]
        self.fill_positions()

    def update_direction(self):
        match self.direction:
            case Direction.UP:
                self.y -= self.GRID_OFFSET
            case Direction.DOWN:
                self.y += self.GRID_OFFSET
            case Direction.LEFT:
                self.x -= self.GRID_OFFSET
            case Direction.RIGHT:
                self.x += self.GRID_OFFSET

    def fill_positions(self):
        self.positions[0] = (self.y, self.x)
        for i in range(1, self.snake_length + 1):
            self.positions[i] = (1, self.x + i * 2)

    def update_position(self):
        self.y = max(1, min(self.y, self.board_height - self.GRID_OFFSET))
        self.x = max(1, min(self.x, self.board_width - self.GRID_OFFSET))
        return self.y, self.x

    def update_snake(self):
        self.y = max(1, min(self.y, self.board_height - self.GRID_OFFSET))
        self.x = max(1, min(self.x, self.board_width - self.GRID_OFFSET))
        self.positions.insert(0, (self.y, self.x))
        self.positions.pop()

    def is_out_of_bounds(self):
        out_of_bounds = (
            self.x <= 0
            or self.x >= self.board_width
            or self.y <= 0
            or self.y >= self.board_height
        )
        return out_of_bounds

    def add_snake_element(self):
        self.update_direction()
        # Prepend to current head position
        self.positions.insert(0, (self.y, self.x))

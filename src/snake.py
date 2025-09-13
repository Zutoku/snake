from snake_element import SnakeElement
from constants import Direction
from typing import List, Tuple


class Snake:
    def __init__(self, y, x, board_height, board_width) -> None:
        self.SNAKE_SHAPE = "#"
        self.board_height = board_height
        self.board_width = board_width
        self.y = y
        self.x = x
        self.direction = Direction.DOWN
        self.snake_length = 5  # TODO: make dynamic, not hardcoded
        self.positions: List[Tuple] = [(0, 0) for _ in range(self.snake_length)]
        self.fill_positions()

    def update_direction(self):
        match self.direction:
            case Direction.UP:
                self.y -= 1
            case Direction.DOWN:
                self.y += 1
            case Direction.LEFT:
                self.x -= 1
            case Direction.RIGHT:
                self.x += 1

    def fill_positions(self):
        self.positions[0] = (self.y, self.x)
        for i in range(1, self.snake_length):
            self.positions[i] = (1, i + 1)

    def update_position(self):
        self.y = max(1, min(self.y, self.board_height))
        self.x = max(1, min(self.x, self.board_width))
        return self.y, self.x

    def update_snake(self):
        self.y = max(1, min(self.y, self.board_height))
        self.x = max(1, min(self.x, self.board_width))
        self.positions.pop()
        self.positions.insert(0, (self.y, self.x))

    def is_out_of_bounds(self):
        out_of_bounds = (
            self.x <= 0
            or self.x >= self.board_width + 1
            or self.y <= 0
            or self.y >= self.board_height + 1
        )
        return out_of_bounds

    def add_snake_element(self):
        self.update_direction()
        # Prepend to current head position
        self.positions.insert(0, (self.y, self.x))

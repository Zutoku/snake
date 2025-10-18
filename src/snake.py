from constants import Direction
from typing import List, Tuple


class Snake:
    def __init__(self, y, x, board_height: int, board_width: int) -> None:
        pass


class SnakeBody:
    def __init__(self, y, x, board_height: int, board_width: int) -> None:
        self.board_height = board_height
        self.board_width = board_width
        self.y = y
        self.x = x

        self.SNAKE_SHAPE = "#"
        self.snake_length: int = 3  # TODO: make dynamic, not hardcoded
        self.positions: List[Tuple] = [(0, 0) for _ in range(self.snake_length)]
        self.growing = False

        self.fill_positions()

    def fill_positions(self) -> None:
        self.positions[0] = (self.y, self.x)
        for i in range(1, self.snake_length):
            self.positions[i] = (1, i + 1)

    def update_snake(self) -> None:
        self.y = max(1, min(self.y, self.board_height))
        self.x = max(1, min(self.x, self.board_width))
        if not self.growing:
            self.positions.pop()
        self.positions.insert(0, (self.y, self.x))
        self.growing = False

    def grow(self):
        self.growing = True


class SnakeMovement:
    def __init__(self) -> None:
        self.direction = Direction.DOWN

    def update_direction(self) -> None:
        match self.direction:
            case Direction.UP:
                self.y -= 1
            case Direction.DOWN:
                self.y += 1
            case Direction.LEFT:
                self.x -= 1
            case Direction.RIGHT:
                self.x += 1


class SnakeCollision:
    def __init__(self, y, x, board_height: int, board_width: int) -> None:
        self.board_height = board_height
        self.board_width = board_width
        self.y = y
        self.x = x

    def is_out_of_bounds(self) -> bool:
        out_of_bounds = (
            self.x <= 0
            or self.x >= self.board_width + 1
            or self.y <= 0
            or self.y >= self.board_height + 1
        )
        return out_of_bounds

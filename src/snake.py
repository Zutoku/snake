from snake_element import SnakeElement
from constants import Direction


class Snake:
    def __init__(self, y, x, board_height, board_width) -> None:
        self.board_height = board_height
        self.board_width = board_width
        self.y = y
        self.x = x
        self.direction = Direction.RIGHT
        self.GRID_OFFSET = 2

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

    def update_position(self):
        self.y = max(1, min(self.y, self.board_height - self.GRID_OFFSET))
        self.x = max(1, min(self.x, self.board_width - self.GRID_OFFSET))
        return self.y, self.x

    def is_out_of_bounds(self):
        out_of_bounds = (
            self.x <= 0
            or self.x >= self.board_width
            or self.y <= 0
            or self.y >= self.board_height
        )
        return out_of_bounds

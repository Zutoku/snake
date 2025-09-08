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

    def update_position(self):
        if not self.out_of_bounds():
            return self.y, self.x

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
        if 0 >= self.x >= self.board_width:
            pass

    def out_of_bounds(self) -> bool:
        return False

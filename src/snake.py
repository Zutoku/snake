from snake_element import SnakeElement
from constants import Direction


class Snake:
    def __init__(self, x, y) -> None:
        self.position = x, y
        self.direction = Direction.RIGHT
        self.GRID_OFFSET = 2

        def update_position(self):
            pass

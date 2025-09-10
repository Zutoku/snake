class SnakeElement:
    def __init__(self, y, x, id=0):
        self.current_position = (y, x)
        self.last_position = (y, x)
        self.id = id

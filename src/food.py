from numpy import random


class Food:
    def __init__(self, game_height, game_width) -> None:
        self.game_height = game_height
        self.game_width = game_width
        self.y = 1
        self.x = 1
        self.position = 0, 0
        self.shape = ""
        self.FOOD_SHAPE = "•"
        self.EMPTY = " "
        self.exists = False

    def generate_food(self):
        self.y = random.randint(1, self.game_height)
        self.x = random.randint(1, self.game_width)
        self.position = self.y, self.x
        self.exists = True

    def eat_food(self):
        self.exists = False

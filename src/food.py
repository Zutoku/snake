from numpy import random


class Food:
    def __init__(self, game_height, game_width) -> None:
        self.game_height = game_height
        self.game_width = game_width
        self.y = 1
        self.x = 1
        self.FOOD_SHAPE = "•"
        self.EMPTY = " "

    def generate_food(self):
        self.y = random.random_integers(1, self.game_height)
        self.x = random.random_integers(1, self.game_width)

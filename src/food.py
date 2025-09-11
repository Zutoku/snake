from numpy import random


class Food:
    def __init__(self, game_height, game_width) -> None:
        self.game_height = game_height
        self.game_width = game_width

    def generate_food(self):
        random.random_integers(1, self.game_height)

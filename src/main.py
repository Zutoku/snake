import time
import pygame
from game_board import GameBoard


def main():
    pygame.init()
    print("Welcome to snake!")
    while True:
        try:
            x = int(input("Please select a game width: "))
            y = int(input("Please select a game height: "))
        except ValueError:
            print("Please only use integers")
            continue
        if 0 < x <= 21 and 0 < y <= 21:
            break
        print("Please choose an integer between 0 and 21")
    game_board = GameBoard(x, y)
    game_board.print_board()

    # game loop starts here:
    running = True
    while running:
        keys = pygame.key.get_just_pressed()
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
        if keys[pygame.K_ESCAPE]:
            running = False


if __name__ == "__main__":
    main()

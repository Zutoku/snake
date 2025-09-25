import curses
import time
from game_board import GameBoard
from snake import Snake
from food import Food
from constants import Direction


class Game:
    def __init__(self, snake_colour, food_colour):
        self.REFRESH_TIMER = 0.5

        self.score: int = 0
        self.snake_colour = snake_colour
        self.food_colour = food_colour

    def run(self, stdscr, game_board: GameBoard, snake: Snake, food: Food):
        start_time = time.time()
        running = True
        hard_mode = True
        while running:
            time_elapsed = time.time() - start_time
            key = stdscr.getch()
            game_board.fill_board()
            # Input handling ---------------------------------------
            match key:
                case 113:  # ASCII code for letter q
                    running = False
                case curses.KEY_UP:
                    snake.direction = Direction.UP
                case curses.KEY_DOWN:
                    snake.direction = Direction.DOWN
                case curses.KEY_LEFT:
                    snake.direction = Direction.LEFT
                case curses.KEY_RIGHT:
                    snake.direction = Direction.RIGHT
            # ------------------------------------------------------

            # Food handling ----------------------------------------
            if food.exists and food.position == snake.positions[0]:
                food.remove_food()
                snake.grow()
                self.score += 1

            if not food.exists:
                food.generate_food()
                while food.position in snake.positions:
                    food.generate_food()
            game_board.set_value(food.y, food.x, food.shape, self.food_colour)
            # --------------------------------------------------------

            # Snake handling -----------------------------------------
            for y, x in snake.positions:
                game_board.set_value(y, x, snake.SNAKE_SHAPE, self.snake_colour)

            if hard_mode:
                if snake.is_out_of_bounds():
                    running = False
                if len(snake.positions) != len(set(snake.positions)):
                    running = False

            if time_elapsed > self.REFRESH_TIMER:
                snake.update_direction()
                snake.update_snake()
                # y, x = snake.update_position()
                start_time = time.time()
            # --------------------------------------------------------

            stdscr.clear()
            game_board.print_board(stdscr)
            stdscr.addstr(f"Current score: {self.score}\n")
            stdscr.refresh()
            # Small delay to reduce CPU usage
            time.sleep(0.1)

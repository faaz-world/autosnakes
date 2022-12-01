from collections import deque
from dataclasses import dataclass
import random


class snake:
    def __init__(self, default_body, default_direction) -> None:
        self.score = 0
        self.totscore = 0
        self.default_position = default_body[0].copy()
        self.default_body = deque(default_body.copy())
        self.default_direction = default_direction
        self.reset()

    def got_apple(self, fruit):
        if self.position == fruit:
            self.score += 10
            return True
        else:
            self.body.pop()
        return False

    def reset(self):
        self.body = self.default_body.copy()
        self.position = self.default_position.copy()
        self.direction = self.default_position
        self.totscore += self.score
        self.score = 0

    def collision(self, other_snake):
        gameover = False
        for part in other_snake.body:
            if part == self.position:
                self.score //= 2
                gameover = True
        return gameover

    def out_of_bounds(self, window_x, window_y):
        out_of_bound = False
        if self.position[0] < 0 or self.position[0] > window_x - 10:
            self.score //= 2
            out_of_bound = True
        if self.position[1] < 0 or self.position[1] >= window_y - 10:
            self.score //= 2
            out_of_bound = True
        return out_of_bound

    def move(self, new_direction):
        @dataclass
        class direction_constant:
            opposite: str
            movement: list

        constants = {
            "UP": direction_constant("DOWN", [0, -10]),
            "DOWN": direction_constant("UP", [0, 10]),
            "LEFT": direction_constant("RIGHT", [-10, 0]),
            "RIGHT": direction_constant("LEFT", [10, 0]),
        }
        if self.direction != constants[new_direction].opposite:
            self.direction = new_direction

        self.position[0] += constants[self.direction].movement[0]
        self.position[1] += constants[self.direction].movement[1]
        self.body.appendleft(self.position.copy())


class snake_states:
    def __init__(self) -> None:
        self.snake1 = snake([[300, 270], [290, 270], [280, 270]], "RIGHT")
        self.snake2 = snake([[300, 330], [310, 330], [320, 330]], "LEFT")
        self.window_x = 600
        self.window_y = 600
        self.generate_fruit()

    def generate_fruit(self):
        self.fruit_position = [
            random.randrange(1, (self.window_x // 10)) * 10,
            random.randrange(1, (self.window_y // 10)) * 10,
        ]

    def reset(self):
        self.snake1.reset()
        self.snake2.reset()
        self.generate_fruit()

    def move(self, snake1_direction, snake2_direction):
        self.snake1.move(snake1_direction)
        self.snake2.move(snake2_direction)
        self.collision_validate()

    def collision_validate(self):
        snake1_gameover = self.snake1.out_of_bounds(
            self.window_x, self.window_y
        ) or self.snake1.collision(self.snake2)
        snake2_gameover = self.snake2.out_of_bounds(
            self.window_x, self.window_y
        ) or self.snake2.collision(self.snake1)
        snake1_has_fruit = self.snake1.got_apple(self.fruit_position)
        snake2_has_fruit = self.snake2.got_apple(self.fruit_position)
        if snake1_has_fruit or snake2_has_fruit:
            self.generate_fruit()
        if snake1_gameover or snake2_gameover:
            self.reset()

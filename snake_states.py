from collections import deque
from dataclasses import dataclass


class snake:
    def __init__(self, default_body, default_direction) -> None:
        self.score = 0
        self.totscore = 0
        self.default_position = default_body[0].copy()
        self.default_body = deque(default_body.copy())
        self.default_direction = default_direction

    def reset(self):
        self.body = self.default_body.copy()
        self.position = self.default_position.copy()
        self.score = 0
        self.direction = self.default_position
        self.totscore += self.score

    def move(self, new_direction):
        @dataclass
        class direction_constant:
            opposite: str
            movement: list

        constants = {
            "UP": direction_constant("DOWN", [0, 10]),
            "DOWN": direction_constant("UP", [0, -10]),
            "LEFT": direction_constant("RIGHT", [-10, 0]),
            "RIGHT": direction_constant("LEFT", [10, 0]),
        }
        if self.direction != constants[new_direction].opposite:
            self.direction = new_direction

        self.position[0] += constants[self.direction].movement[0]
        self.position[1] += constants[self.direction].movement[1]
        self.body.appendleft(self.position)


class snake_states:
    def __init__(self) -> None:
        self.snake1_totscore = 0
        self.snake2_totscore = 0
        self.snake1 = snake([[300, 270], [290, 270], [280, 270]], "RIGHT")
        self.snake2 = snake([[300, 330], [310, 330], [320, 330]], "LEFT")
        self.window_x = 600
        self.window_y = 600
        self.opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}

    def reset(self):
        self.snake1.reset()
        self.snake2.reset()

    def move(self, snake1_direction, snake2_direction):
        self.snake1.move(snake1_direction)
        self.snake2.move(snake2_direction)

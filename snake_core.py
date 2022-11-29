# importing libraries
import pygame
import time
import random
import teams
from teams import *

# Custom Imports from Pungi
import math

snake_speed = 15

team1_name = "copperhead"
# team2_name = "beta"
team2_name = "side_winder"

player1 = getattr(teams, team1_name)
player2 = getattr(teams, team2_name)

# Window size
window_x = 600
window_y = 600

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = (255, 255, 102)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption("Z-Auto Snakes")
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake1_init_position = [300, 270]
snake2_init_position = [300, 330]

snake1_position = snake1_init_position.copy()
snake2_position = snake2_init_position.copy()

# defining first 3 blocks of snake body. Snakes start in the center of the screen
snake1_init_body = [[300, 270], [290, 270], [280, 270]]
snake2_init_body = [[300, 330], [310, 330], [320, 330]]

snake1_body = snake1_init_body.copy()
snake2_body = snake2_init_body.copy()

# fruit position
fruit_position = [
    random.randrange(1, (window_x // 10)) * 10,
    random.randrange(1, (window_y // 10)) * 10,
]

fruit_spawn = True
running = True
# setting default snake direction away from each other

snake1_direction = "RIGHT"
snake1_change_to = snake1_direction

snake2_direction = "LEFT"
snake2_change_to = snake2_direction


# initial score
snake1_score = 0
snake2_score = 0
snake1_totscore = 0
snake2_totscore = 0


# displaying Score function
def show_score(choice, color, font, size):

    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface1 = score_font.render(
        "Snake 1: "
        + team1_name
        + " "
        + str(snake1_score)
        + " Total:"
        + str(snake1_totscore),
        True,
        green,
    )

    score_surface2 = score_font.render(
        "Snake 2: "
        + team2_name
        + " "
        + str(snake2_score)
        + " Total:"
        + str(snake2_totscore),
        True,
        yellow,
    )

    time_surface = score_font.render(
        " Time: " + str(int(600 - (pygame.time.get_ticks() / 1000))),
        True,
        color,
    )
    # create a rectangular object for the text
    # surface object
    score_rect1 = score_surface1.get_rect()
    score_rect2 = score_surface2.get_rect()
    time_rect = time_surface.get_rect()
    # displaying text
    game_window.blit(score_surface1, (0, 0))
    game_window.blit(score_surface2, (0, 20))
    game_window.blit(time_surface, (0, window_y - 20))


# Reset after a crash
def next_round():

    game_window.fill(red)

    # add up total points
    global snake1_totscore
    global snake2_totscore
    global snake1_score
    global snake2_score

    snake1_totscore += snake1_score
    snake2_totscore += snake2_score
    snake1_score = 0
    snake2_score = 0

    # reset snake default position
    global snake1_position
    global snake2_position
    snake1_position = snake1_init_position.copy()
    snake2_position = snake2_init_position.copy()

    # reset first 4 blocks of snake body
    global snake1_body
    global snake2_body
    snake1_body = snake1_init_body.copy()
    snake2_body = snake2_init_body.copy()

    # setting default snake direction towards
    # right
    global snake1_direction
    snake1_direction = "RIGHT"

    global snake2_direction
    snake2_direction = "LEFT"

    # randomize fruit position
    global fruit_spawn
    fruit_spawn = False
    return


# game over function
def game_over():

    # assign final points
    global snake1_totscore
    global snake2_totscore
    snake1_totscore += snake1_score
    snake2_totscore += snake2_score

    # creating font object my_font
    my_font = pygame.font.SysFont("times new roman", 20)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        "Final Score! Snake 1 : "
        + str(snake1_totscore)
        + " -- Snake 2 : "
        + str(snake2_totscore),
        True,
        red,
    )

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 2 seconds we will quit the program
    time.sleep(20)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()


# Main Function
while running:

    if pygame.time.get_ticks() > 600000:
        running = False
    # handling key events manual override
    snake1_change_to = player1(
        snake1_body,
        snake2_body,
        fruit_position,
        snake1_direction,
        snake2_direction,
        snake1_position,
        snake2_position,
        window_x,
        window_y,
    )
    snake2_change_to = player2(
        snake2_body,
        snake1_body,
        fruit_position,
        snake2_direction,
        snake1_direction,
        snake2_position,
        snake1_position,
        window_x,
        window_y,
    )

    # handling key events manual override

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake1_change_to = "UP"
            if event.key == pygame.K_DOWN:
                snake1_change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                snake1_change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                snake1_change_to = "RIGHT"
            if event.key == pygame.K_w:
                snake2_change_to = "UP"
            if event.key == pygame.K_s:
                snake2_change_to = "DOWN"
            if event.key == pygame.K_a:
                snake2_change_to = "LEFT"
            if event.key == pygame.K_d:
                snake2_change_to = "RIGHT"
        if event.type == pygame.QUIT:
            running = False

    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if snake1_change_to == "UP" and snake1_direction != "DOWN":
        snake1_direction = "UP"
    if snake1_change_to == "DOWN" and snake1_direction != "UP":
        snake1_direction = "DOWN"
    if snake1_change_to == "LEFT" and snake1_direction != "RIGHT":
        snake1_direction = "LEFT"
    if snake1_change_to == "RIGHT" and snake1_direction != "LEFT":
        snake1_direction = "RIGHT"
    if snake2_change_to == "UP" and snake2_direction != "DOWN":
        snake2_direction = "UP"
    if snake2_change_to == "DOWN" and snake2_direction != "UP":
        snake2_direction = "DOWN"
    if snake2_change_to == "LEFT" and snake2_direction != "RIGHT":
        snake2_direction = "LEFT"
    if snake2_change_to == "RIGHT" and snake2_direction != "LEFT":
        snake2_direction = "RIGHT"

    # Moving the snakes
    if snake1_direction == "UP":
        snake1_position[1] -= 10
    if snake1_direction == "DOWN":
        snake1_position[1] += 10
    if snake1_direction == "LEFT":
        snake1_position[0] -= 10
    if snake1_direction == "RIGHT":
        snake1_position[0] += 10
    if snake2_direction == "UP":
        snake2_position[1] -= 10
    if snake2_direction == "DOWN":
        snake2_position[1] += 10
    if snake2_direction == "LEFT":
        snake2_position[0] -= 10
    if snake2_direction == "RIGHT":
        snake2_position[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake1_body.insert(0, list(snake1_position))
    snake2_body.insert(0, list(snake2_position))

    # Grow Snake 1 if it colides with fruit
    if (
        snake1_position[0] == fruit_position[0]
        and snake1_position[1] == fruit_position[1]
    ):
        snake1_score += 10
        fruit_spawn = False
    else:
        snake1_body.pop()

        # Grow Snake 2 if it colides with fruit
    if (
        snake2_position[0] == fruit_position[0]
        and snake2_position[1] == fruit_position[1]
    ):
        snake2_score += 10
        fruit_spawn = False
    else:
        snake2_body.pop()

    if not fruit_spawn:
        fruit_position = [
            random.randrange(1, (window_x // 10)) * 10,
            random.randrange(1, (window_y // 10)) * 10,
        ]

    fruit_spawn = True
    game_window.fill(black)

    # Draw Snake 1 body
    for pos in snake1_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        # Draw Snake 2 body
    for pos in snake2_body:
        pygame.draw.rect(game_window, yellow, pygame.Rect(pos[0], pos[1], 10, 10))
        # Draw Fruit
    pygame.draw.rect(
        game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10)
    )

    # Game Over conditions
    if snake1_position[0] < 0 or snake1_position[0] > window_x - 10:
        snake1_score /= 2
        snake1_totscore /= 2
        next_round()
    if snake1_position[1] < 0 or snake1_position[1] > window_y - 10:
        snake1_score /= 2
        snake1_totscore /= 2
        next_round()

    # Game Over conditions
    if snake2_position[0] < 0 or snake2_position[0] > window_x - 10:
        snake2_score /= 2
        snake2_totscore /= 2
        next_round()
    if snake2_position[1] < 0 or snake2_position[1] > window_y - 10:
        snake2_score /= 2
        snake2_totscore /= 2
        next_round()

    # Coliding with own snake body
    for block in snake1_body[1:]:
        if snake1_position[0] == block[0] and snake1_position[1] == block[1]:
            snake1_score /= 2
            next_round()
    for block in snake2_body[1:]:
        if snake2_position[0] == block[0] and snake2_position[1] == block[1]:
            snake2_score /= 2
            next_round()

    # Coliding with other snake body
    for block in snake1_body[1:]:
        if snake2_position[0] == block[0] and snake2_position[1] == block[1]:
            snake2_score /= 2
            next_round()
    for block in snake2_body[1:]:
        if snake1_position[0] == block[0] and snake1_position[1] == block[1]:
            snake1_score /= 2
            next_round()

    # displaying score countinuously
    show_score(1, white, "times new roman", 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)


game_over()

# importing libraries
import pygame
import time
import random
import teams
from teams import *
import snake_states

# Custom Imports from Pungi
import math

snake_speed = 15

team1_name = "copperhead"
# team2_name = "beta"
team2_name = "side_winder"

player1 = getattr(teams, team1_name)
player2 = getattr(teams, team2_name)

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


running = True
# setting default snake direction away from each other


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
        + str(board.snake1.score)
        + " Total:"
        + str(board.snake1.totscore),
        True,
        green,
    )

    score_surface2 = score_font.render(
        "Snake 2: "
        + team2_name
        + " "
        + str(board.snake2.score)
        + " Total:"
        + str(board.snake2.totscore),
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


# game over function
def game_over():

    # creating font object my_font
    my_font = pygame.font.SysFont("times new roman", 20)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        "Final Score! Snake 1 : "
        + str(board.snake1.totscore)
        + " -- Snake 2 : "
        + str(board.snake2.totscore),
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


board = snake_states.snake_states()
# Main Function
while running:

    if pygame.time.get_ticks() > 600000:
        running = False
    # handling key events manual override
    snake1_change_to = player1(
        list(board.snake1.body),
        list(board.snake2.body),
        board.fruit_position,
        board.snake1.direction,
        board.snake2.direction,
        board.snake1.position,
        board.snake2.position,
        board.window_x,
        board.window_y,
    )
    snake2_change_to = player2(
        list(board.snake2.body),
        list(board.snake1.body),
        board.fruit_position,
        board.snake2.direction,
        board.snake1.direction,
        board.snake2.position,
        board.snake1.position,
        board.window_x,
        board.window_y,
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
    board.move(snake1_change_to, snake2_change_to)

    game_window.fill(black)

    # Draw Snake 1 body
    for pos in board.snake1.body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        # Draw Snake 2 body
    for pos in board.snake2.body:
        pygame.draw.rect(game_window, yellow, pygame.Rect(pos[0], pos[1], 10, 10))
        # Draw Fruit
    pygame.draw.rect(
        game_window,
        white,
        pygame.Rect(board.fruit_position[0], board.fruit_position[1], 10, 10),
    )

    # displaying score countinuously
    show_score(1, white, "times new roman", 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)


game_over()

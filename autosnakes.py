import pygame
import time
import random
from player1 import * 
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 1600
dis_height = 800
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Auto Snakes')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 15)
score_font = pygame.font.SysFont("comicsansms", 15)
 
 
def Your_score(score_p1, score_p2):
    value1 = score_font.render("Your Score: " + str(score_p1), True, yellow)
    value2 = score_font.render("Your Score: " + str(score_p2), True, yellow)
    dis.blit(value1, [0, 0])
    score_width , score_height = score_font.size("Your Score: " + str(score_p2))
    dis.blit(value2, [(dis_width-score_width),0])
 
 
 
def draw_snake(snake_block, snake_list, snake_color):
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 4
    y1 = dis_height / 2
 
    x2 = (dis_width / 4)+(dis_width / 2)
    y2 = dis_height / 2

    x1_change = 0
    y1_change = 0

    x2_change = 0
    y2_change = 0
 
    snake_List_p1 = []
    Length_of_snake_p1 = 1

    snake_List_p2 = []
    Length_of_snake_p2 = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake_p1 - 1,Length_of_snake_p2 - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        x1_change, y1_change = auto_play_p1(snake_block, snake_List_p1, snake_List_p2, foodx, foody,x1_change,y1_change,x1,y1,dis_width,dis_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_w:
                    y2_change = -snake_block
                    x2_change = 0
                elif event.key == pygame.K_a:
                    y2_change = 0
                    x2_change = -snake_block
                elif event.key == pygame.K_d:
                    y2_change = 0
                    x2_change = snake_block
                elif event.key == pygame.K_s:
                    y2_change = snake_block
                    x2_change = 0


        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        if x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        x2 += x2_change
        y2 += y2_change

        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head_p1 = []
        snake_Head_p1.append(x1)
        snake_Head_p1.append(y1)
        snake_List_p1.append(snake_Head_p1)

        snake_Head_p2 = []
        snake_Head_p2.append(x2)
        snake_Head_p2.append(y2)
        snake_List_p2.append(snake_Head_p2)

        if len(snake_List_p1) > Length_of_snake_p1:
            del snake_List_p1[0]
        if len(snake_List_p2) > Length_of_snake_p2:
            del snake_List_p2[0]

        for x in snake_List_p1[:-1]:
            if x == snake_Head_p1:
                game_close = True
 
        for x in snake_List_p2[:-1]:
            if x == snake_Head_p2:
                game_close = True

        draw_snake(snake_block, snake_List_p1, black)
        draw_snake(snake_block, snake_List_p2, red)
        Your_score(Length_of_snake_p1 - 1,Length_of_snake_p2 - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake_p1 += 1

        if x2 == foodx and y2 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake_p2 += 1

        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
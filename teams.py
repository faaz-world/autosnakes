from functions import *


def alpha(mysnake, othersnake, fruit, mysnake_dir, othersnake_dir, mysnake_pos, othersnake_pos, dis_width, dis_height):
    new_direction = mysnake_dir
    mysnake_new_position_x = mysnake_pos[0]
    mysnake_new_position_y = mysnake_pos[1]

    # new_direction = check_before_self_collision(mysnake, dis_width, fruit, mysnake_dir)
    # if not new_direction:
    #     new_direction = change_auto_direction(mysnake, fruit, mysnake_dir)
    #     # new_direction = "RIGHT"
    # else:
    #     print("Collide")

    # new_direction = check_other_snake_collision(mysnake,othersnake,dis_width,fruit,mysnake_dir)

    new_direction = get_direction(mysnake, othersnake, dis_width, fruit, mysnake_dir)

    # Moving the snakes
    if new_direction == 'UP':
        mysnake_new_position_y -= 10
    if new_direction == 'DOWN':
        mysnake_new_position_y += 10
    if new_direction == 'LEFT':
        mysnake_new_position_x -= 10
    if new_direction == 'RIGHT':
        mysnake_new_position_x += 10

    # avoid left wall 
    if mysnake_new_position_x < 0:  # hitting left wall
        new_direction = 'UP'

    # avoid left wall
    if mysnake_new_position_x > dis_width - 10 and mysnake_new_position_y < fruit[1]:  # hitting left wall
        new_direction = 'DOWN'

    # avoid left right
    elif mysnake_new_position_x > dis_width - 10:  # hitting left wall
        new_direction = 'UP'

    # avoid left wall
    if mysnake_new_position_y > dis_height - 10:  # hitting left wall
        new_direction = 'LEFT'
    # avoid up wall
    if mysnake_new_position_y < 0:  # hitting left wall
        new_direction = 'LEFT'

    return new_direction


def beta(mysnake, othersnake, fruit, mysnake_dir, othersnake_dir, mysnake_pos, othersnake_pos, dis_width, dis_height):
    new_direction = mysnake_dir
    mysnake_new_position_x = mysnake_pos[0]
    mysnake_new_position_y = mysnake_pos[1]

    # Moving the snakes
    if mysnake_dir == 'UP':
        mysnake_new_position_y -= 10
    if mysnake_dir == 'DOWN':
        mysnake_new_position_y += 10
    if mysnake_dir == 'LEFT':
        mysnake_new_position_x -= 10
    if mysnake_dir == 'RIGHT':
        mysnake_new_position_x += 10

    # avoid left wall 
    if mysnake_new_position_x < 0:  # hitting left wall
        new_direction = 'UP'
    # avoid left right 
    if mysnake_new_position_x > dis_width - 10:  # hitting left wall
        new_direction = 'UP'
    # avoid left wall 
    if mysnake_new_position_y < 0:  # hitting left wall
        new_direction = 'LEFT'
    # avoid left wall 
    if mysnake_new_position_y > dis_height - 10:  # hitting left wall
        new_direction = 'LEFT'

    return new_direction

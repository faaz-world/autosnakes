import math


def alpha(
    mysnake,
    othersnake,
    fruit,
    mysnake_dir,
    othersnake_dir,
    mysnake_pos,
    othersnake_pos,
    dis_width,
    dis_height,
):

    new_direction = mysnake_dir
    mysnake_new_position_x = mysnake_pos[0]
    mysnake_new_position_y = mysnake_pos[1]

    # Moving the snakes
    if mysnake_dir == "UP":
        mysnake_new_position_y -= 10
    if mysnake_dir == "DOWN":
        mysnake_new_position_y += 10
    if mysnake_dir == "LEFT":
        mysnake_new_position_x -= 10
    if mysnake_dir == "RIGHT":
        mysnake_new_position_x += 10

    # avoid left wall
    if mysnake_new_position_x < 0:  # hitting left wall
        new_direction = "UP"
    # avoid left right
    if mysnake_new_position_x > dis_width - 10:  # hitting left wall
        new_direction = "UP"
    # avoid left wall
    if mysnake_new_position_y < 0:  # hitting left wall
        new_direction = "LEFT"
    # avoid left wall
    if mysnake_new_position_y > dis_height - 10:  # hitting left wall
        new_direction = "LEFT"

    return new_direction


def beta(
    mysnake,
    othersnake,
    fruit,
    mysnake_dir,
    othersnake_dir,
    mysnake_pos,
    othersnake_pos,
    dis_width,
    dis_height,
):

    new_direction = mysnake_dir
    mysnake_new_position_x = mysnake_pos[0]
    mysnake_new_position_y = mysnake_pos[1]

    # Moving the snakes
    if mysnake_dir == "UP":
        mysnake_new_position_y -= 10
    if mysnake_dir == "DOWN":
        mysnake_new_position_y += 10
    if mysnake_dir == "LEFT":
        mysnake_new_position_x -= 10
    if mysnake_dir == "RIGHT":
        mysnake_new_position_x += 10

    # avoid left wall
    if mysnake_new_position_x < 0:  # hitting left wall
        new_direction = "UP"
    # avoid left right
    if mysnake_new_position_x > dis_width - 10:  # hitting left wall
        new_direction = "UP"
    # avoid left wall test
    if mysnake_new_position_y < 0:  # hitting left wall
        new_direction = "LEFT"
    # avoid left wall
    if mysnake_new_position_y > dis_height - 10:  # hitting left wall
        new_direction = "LEFT"

    return new_direction

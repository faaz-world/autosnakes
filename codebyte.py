#from snake_core import *
from enum import Enum
from collections import deque
from numpy import sqrt



def code_byte(
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

    


    #avoid enemy


    if (mysnake_new_position_x==othersnake_pos[0]) and (othersnake_pos[1]>(mysnake_new_position_y-50)):

        if (mysnake_new_position_x==fruit[0] and mysnake_new_position_y>fruit[1]) or (mysnake_new_position_x<fruit[0] and mysnake_new_position_y==fruit[1]):
            mysnake_dir = "UP"
        elif (mysnake_new_position_x==fruit[0] and mysnake_new_position_y<fruit[1]) or (mysnake_new_position_x>fruit[0] and mysnake_new_position_y==fruit[1]):
            mysnake_dir = "DOWN"

        elif (mysnake_new_position_x >fruit[0] and mysnake_new_position_y>fruit[1]) or (mysnake_new_position_x >fruit[0] and mysnake_new_position_y<fruit[1]) or (mysnake_new_position_y==fruit[1] and mysnake_new_position_x >fruit[0]):
            mysnake_dir = "LEFT"

        elif (mysnake_new_position_x <fruit[0] and mysnake_new_position_y<fruit[1]) or (mysnake_new_position_x <fruit[0] and mysnake_new_position_y>fruit[1]) or (mysnake_new_position_y==fruit[1] and mysnake_new_position_x <fruit[0]):
            mysnake_dir = "RIGHT"
           

        new_direction = mysnake_dir
        
    elif (mysnake_new_position_y==othersnake_pos[1]) and (othersnake_pos[0]>(mysnake_new_position_x+50)):

        if (mysnake_new_position_x==fruit[0] and mysnake_new_position_y>fruit[1]) or (mysnake_new_position_x<fruit[0] and mysnake_new_position_y==fruit[1]):
            mysnake_dir = "UP"
        elif (mysnake_new_position_x==fruit[0] and mysnake_new_position_y<fruit[1]) or (mysnake_new_position_x>fruit[0] and mysnake_new_position_y==fruit[1]):
            mysnake_dir = "DOWN"

        elif (mysnake_new_position_x >fruit[0] and mysnake_new_position_y>fruit[1]) or (mysnake_new_position_x >fruit[0] and mysnake_new_position_y<fruit[1]) or (mysnake_new_position_y==fruit[1] and mysnake_new_position_x >fruit[0]):
            mysnake_dir = "LEFT"

        elif (mysnake_new_position_x <fruit[0] and mysnake_new_position_y<fruit[1]) or (mysnake_new_position_x <fruit[0] and mysnake_new_position_y>fruit[1]) or (mysnake_new_position_y==fruit[1] and mysnake_new_position_x <fruit[0]):
            mysnake_dir = "RIGHT"
           

        new_direction = mysnake_dir

    elif (mysnake_new_position_y==othersnake_pos[1]) and (othersnake_pos[0]<(mysnake_new_position_x-50)): 

        if (mysnake_new_position_x==fruit[0] and mysnake_new_position_y>fruit[1]) or (mysnake_new_position_x<fruit[0] and mysnake_new_position_y==fruit[1]):
            mysnake_dir = "UP"
        elif (mysnake_new_position_x==fruit[0] and mysnake_new_position_y<fruit[1]) or (mysnake_new_position_x>fruit[0] and mysnake_new_position_y==fruit[1]):
            mysnake_dir = "DOWN"

        elif (mysnake_new_position_x >fruit[0] and mysnake_new_position_y>fruit[1]) or (mysnake_new_position_x >fruit[0] and mysnake_new_position_y<fruit[1]) or (mysnake_new_position_y==fruit[1] and mysnake_new_position_x >fruit[0]):
            mysnake_dir = "LEFT"

        elif (mysnake_new_position_x <fruit[0] and mysnake_new_position_y<fruit[1]) or (mysnake_new_position_x <fruit[0] and mysnake_new_position_y>fruit[1]) or (mysnake_new_position_y==fruit[1] and mysnake_new_position_x <fruit[0]):
            mysnake_dir = "RIGHT"
           

        new_direction = mysnake_dir   

    else: 

        if (mysnake_new_position_x==fruit[0] and mysnake_new_position_y>fruit[1]) or (mysnake_new_position_x<fruit[0] and mysnake_new_position_y==fruit[1]):
            mysnake_dir = "UP"
        elif (mysnake_new_position_x==fruit[0] and mysnake_new_position_y<fruit[1]) or (mysnake_new_position_x>fruit[0] and mysnake_new_position_y==fruit[1]):
            mysnake_dir = "DOWN"

        elif (mysnake_new_position_x >fruit[0] and mysnake_new_position_y>fruit[1]) or (mysnake_new_position_x >fruit[0] and mysnake_new_position_y<fruit[1]) or (mysnake_new_position_y==fruit[1] and mysnake_new_position_x >fruit[0]):
            mysnake_dir = "LEFT"

        elif (mysnake_new_position_x <fruit[0] and mysnake_new_position_y<fruit[1]) or (mysnake_new_position_x <fruit[0] and mysnake_new_position_y>fruit[1]) or (mysnake_new_position_y==fruit[1] and mysnake_new_position_x <fruit[0]):
            mysnake_dir = "RIGHT"
           

        new_direction = mysnake_dir

    # Moving the snakes
    if mysnake_dir == "UP":
        mysnake_new_position_y -= 10
    if mysnake_dir == "DOWN":
        mysnake_new_position_y += 10
    if mysnake_dir == "LEFT":
        mysnake_new_position_x -= 10
    if mysnake_dir == "RIGHT":
        mysnake_new_position_x += 10   

    #avoid walls
    
    if mysnake_new_position_x < 0 and mysnake_new_position_y < fruit[1]:  
         new_direction = 'UP'

     # avoid left wall
    if mysnake_new_position_x > dis_width - 10 and mysnake_new_position_y > fruit[1]:  
         new_direction = 'RIGHT'

     # avoid left right
    elif mysnake_new_position_x > dis_width - 10 and mysnake_new_position_y < fruit[1]:  
        new_direction = 'UP'

    # avoid left wall
    if mysnake_new_position_y > dis_height - 10 and mysnake_new_position_x < fruit[0]:  
         new_direction = 'LEFT'
     # avoid up wall
    if mysnake_new_position_y < 0 and mysnake_new_position_x < fruit[0]:  
         new_direction = 'LEFT'
    
    return new_direction



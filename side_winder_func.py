import math 


def side_winder( mysnake, othersnake, fruit, mysnake_dir, othersnake_dir, mysnake_pos, othersnake_pos, dis_width, dis_height ):


    mysnake_new_position_x = mysnake_pos[0]
    mysnake_new_position_y = mysnake_pos[1]
    if mysnake_new_position_x==fruit[0] and mysnake_new_position_y>fruit[1]:
        mysnake_dir = "UP"
    elif mysnake_new_position_x==fruit[0] and mysnake_new_position_y<fruit[1]:
        mysnake_dir = "DOWN"
    elif mysnake_new_position_y==fruit[1] and mysnake_new_position_x >fruit[0]:
        mysnake_dir = "LEFT"
    elif mysnake_new_position_y==fruit[1] and mysnake_new_position_x <fruit[0]:
        mysnake_dir = "RIGHT"
    elif mysnake_new_position_x >fruit[0] and mysnake_new_position_y>fruit[1]:
        mysnake_dir = "LEFT"
    elif mysnake_new_position_x >fruit[0] and mysnake_new_position_y<fruit[1]:
        mysnake_dir = "LEFT"
    elif mysnake_new_position_x <fruit[0] and mysnake_new_position_y<fruit[1]:
        mysnake_dir = "RIGHT"
    elif mysnake_new_position_x <fruit[0] and mysnake_new_position_y>fruit[1]:
        mysnake_dir = "RIGHT"
    

	# Moving the snakes
 
    # avoid left wall 
    if mysnake_new_position_x < 10: #hitting left wall 
       mysnake_dir= 'RIGHT'
    # avoid left right 
    if mysnake_new_position_x > dis_width-10: 
       mysnake_dir= 'LEFT'
    # avoid left wall 
    if mysnake_new_position_y <10: 
       mysnake_dir= 'DOWN'
    # avoid left wall 
    if mysnake_new_position_y > dis_height-10: 
       mysnake_dir= 'UP'
		
    return mysnake_dir
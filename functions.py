

def change_auto_direction(mysnake,fruit,mysnake_dir):
    if mysnake[0][0] == fruit[0]:
       if mysnake[0][1] < fruit[1]:
          if mysnake_dir !='UP':
             return 'DOWN'
          else:
             return 'LEFT' 
       else:
          if mysnake_dir != 'DOWN':
            return 'UP'
          else:
            return 'LEFT' 
    elif mysnake[0][1] == fruit[1]:  
        if mysnake[0][0] < fruit[0]:
            if mysnake_dir !='LEFT':
                return 'RIGHT'
            else:
                return 'UP'
        else:
            if mysnake_dir !='RIGHT':
                return 'LEFT'
            else:
                return 'UP'
    elif mysnake[0][1]  < fruit[1] and mysnake[0][1] < fruit[1]:
        if mysnake_dir != 'LEFT':
            return 'RIGHT'  
        else:
            return 'DOWN'
    elif mysnake[0][1] < fruit[1] and mysnake[0][1] > fruit[1]: 
        if mysnake_dir !='LEFT':
            return 'RIGHT'
        else:
            return 'UP'   
    elif mysnake[0][1]  > fruit[1] and mysnake[0][1] < fruit[1]: 
        if mysnake_dir != 'RIGHT':
            return 'LEFT'
        else:
            return 'DOWN'
    elif mysnake[0][1]  > fruit[1] and mysnake[0][1] > fruit[1]: 
        if mysnake_dir != 'RIGHT':
            return 'LEFT'
        else:
            return 'UP'          


def check_before_self_collision(mysnake,dis_width,fruit,mysnake_dir):
    for block in mysnake[1:]:
        if mysnake_dir == "UP":
            diff = mysnake[0][1] - block[1]
            print(diff)
            if 0 < diff <= 20 and mysnake[0][0] == block[0]:
                if mysnake[0][0] < fruit[0]:
                    print("right")
                    if not is_snake_collision_right(mysnake,dis_width):
                        return 'RIGHT'
                        
                    else:
                        return 'LEFT'
                    
                else:
                    print("left")
                    if not is_snake_collision_left(mysnake,dis_width):
                        return 'LEFT'
                        
                    else:
                        return 'RIGHT'

            elif mysnake_dir == "DOWN":
                diff = block[1] - mysnake[0][1]
                if 0 < diff <= 2 and mysnake[0][0] == block[0]:
                    if mysnake[0][0] < fruit[0]:
                        if not is_snake_collision_right(mysnake,dis_width):
                            return 'RIGHT'
                            
                        else:
                            return 'LEFT'
                            
                    else:
                        if not is_snake_collision_left(mysnake,dis_width):
                            return 'LEFT'
                            
                        else:
                            return 'RIGHT'
                            
            elif mysnake_dir == "LEFT":
                diff = mysnake[0][0] - block[0]
                if 0 < diff <= 20 and mysnake[0][1] == block[0]:
                    if mysnake[0][1] < fruit[1]:
                        if not is_snake_collision_down(mysnake,dis_width):
                            return 'DOWN'
                            
                        else:
                            return 'UP'
                            
                    else:
                        if not is_snake_collision_up(mysnake,dis_width):
                            return 'UP'
                            
                        else:
                            return 'DOWN'
                            
            elif mysnake_dir == "RIGHT":
                diff = block[0] - mysnake[0][0]
                if 0 < diff <= 20 and mysnake[0][1] == block[0]:
                    if mysnake[0][1] < fruit[1]:
                        if not is_snake_collision_down(mysnake,dis_width):
                            return 'DOWN'
                            
                        else:
                            return 'UP'
                            
                    else:
                        if not is_snake_collision_up(mysnake,dis_width):
                            return 'UP'
                            
                        else:
                            return 'DOWN'
                            
                        

def is_snake_collision_right(mysnake,dis_width):
    my_x_pos = int(mysnake[0][0])
    my_y_pos = int(mysnake[0][1])
    while my_x_pos < dis_width:
        for block in mysnake[1:]:
            if block[0] == my_x_pos and block[1] == my_y_pos:
                return True
        my_x_pos += 1
    return False    

def is_snake_collision_left(mysnake,dis_width):
    my_x_pos = int(mysnake[0][0])
    my_y_pos = int(mysnake[0][1])
    while my_x_pos > 0:
        for block in mysnake[1:]:
            if block[0] == my_x_pos and block[1] == my_y_pos:
                return True
        my_x_pos -= 1
    return False

def is_snake_collision_up(mysnake):
        my_x_pos = int(mysnake[0][0])
        my_y_pos = int(mysnake[0][1])
        while my_y_pos > 0:
            for block in mysnake[1:]:
                if block.y == my_y_pos and block.x == my_x_pos:
                    return True
            my_y_pos -= 1
        return False

def is_snake_collision_down(mysnake,dis_width):
    my_x_pos = int(mysnake[0][0])
    my_y_pos = int(mysnake[0][1])
    while my_y_pos < dis_width:
        for block in mysnake[1:]:
            if block.y == my_y_pos and block.x == my_x_pos:
                return True
        my_y_pos += 1
    return False         
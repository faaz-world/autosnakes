import math

def auto_play_p1(snake_block, snake_list_p1, snake_list_p2, food_x, food_y,x1_change,y1_change,x1,y1,dis_width,dis_height):

    newx1 = x1+x1_change
    newy1 = y1+y1_change
    

    ## Avoid Edges
    if newx1 >= dis_width :   ## reached right edge 
        if y1_change-snake_block >0:   ## check if can go up 
            y1_change = -snake_block
            x1_change = 0
        elif y1_change+snake_block < dis_height: 
            y1_change = +snake_block
            x1_change = 0            
        else: 
            y1_change = -snake_block
            x1_change = 0

    if  newx1 < 0:   ## reached left 
        if y1_change-snake_block >0: 
            y1_change = -snake_block
            x1_change = 0
        elif y1_change+snake_block >dis_height:
            y1_change = +snake_block
            x1_change = 0              
        else: 
            y1_change = -snake_block
            x1_change = 0   

    if newy1 >= dis_height :  ## reached bottom 
        if x1_change-snake_block >0:   ## check if it can go left if not
            x1_change = -snake_block
            y1_change = 0
        elif x1_change+snake_block >dis_width:    ## check if it can go right 
            x1_change = +snake_block
            y1_change = 0
        else: 
            x1_change = -snake_block ## go left anyway 
            y1_change = 0

    if  newy1 < 0:  ## reached top 
        if x1_change-snake_block >0: 
            x1_change = -snake_block
            y1_change = 0
        elif x1_change+snake_block < dis_width:
            x1_change = +snake_block
            y1_change = 0             
        else: 
            x1_change = -snake_block
            y1_change = 0

    point1 = [food_x,food_y] 
    point2 = [x1,y1]
    point3 = [newx1,newy1]

    eval1 = math.dist(point1,point2)
    eval2 = math.dist(point1,point3)

    if eval2 < eval1:
        print ("Good")
    else: 
        print ("Bad")
        

    return x1_change, y1_change 
 
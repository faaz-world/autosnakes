def auto_play_p1(snake_block, snake_list_p1, snake_list_p2, food_x, food_y,x1_change,y1_change,x1,y1,dis_width,dis_height):

    newx1 = x1+x1_change
    newy1 = y1+y1_change
    
    if newx1 >= dis_width or newx1 < 0:
        y1_change = -snake_block
        x1_change = 0
    elif newy1 >= dis_height or newy1 < 0:
        x1_change = -snake_block
        y1_change = 0            
    return x1_change, y1_change 
 
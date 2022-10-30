

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
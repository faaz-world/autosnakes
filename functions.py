IS_COLLISION_DETECTED = False
IS_OTHERSNAKE_COLLISION_DETECTED = False


def change_auto_direction(mysnake, fruit, mysnake_dir, dis_width):
    if mysnake[0][0] == fruit[0]:
        if mysnake[0][1] < fruit[1]:
            if mysnake_dir != 'UP':
                print("5. Down")
                return 'DOWN'
            else:
                if mysnake[0][0] != 0:
                    print("6. Left")
                    return 'LEFT'
                else:
                    print("6. Right")
                    return 'RIGHT'
        else:
            if mysnake_dir != 'DOWN':
                print("7. UP")
                return 'UP'
            else:
                if mysnake[0][0] != 0:
                    print("8. Left")
                    return 'LEFT'
                else:
                    print("8. Right")
                    return 'RIGHT'
    elif mysnake[0][1] == fruit[1]:
        if mysnake[0][0] < fruit[0]:
            if mysnake_dir != 'LEFT':
                print("9. Right")
                return 'RIGHT'
            else:
                if mysnake[0][1] != 0:
                    print("10. Up")
                    return 'UP'
                else:
                    print("10. Down")
                    return 'DOWN'
        else:
            if mysnake_dir != 'RIGHT':
                print("11. Left")
                return 'LEFT'
            else:
                if mysnake[0][1] != 0:
                    print("12. Up")
                    return 'UP'
                else:
                    print("12. Down")
                    return 'DOWN'
    elif mysnake[0][0] < fruit[0] and mysnake[0][1] < fruit[1]:
        if mysnake_dir != 'LEFT':
            print("1. Right")
            return 'RIGHT'
        else:
            print("1. Down")
            return 'DOWN'
    elif mysnake[0][0] < fruit[0] and mysnake[0][1] > fruit[1]:
        if mysnake_dir != 'LEFT':
            print("2. Right")
            return 'RIGHT'
        else:
            print("2. Up")
            return 'UP'
    elif mysnake[0][0] > fruit[0] and mysnake[0][1] < fruit[1]:
        if mysnake_dir != 'RIGHT':
            print("3. Left")
            return 'LEFT'
        else:
            print("3. Down")
            return 'DOWN'
    elif mysnake[0][0] > fruit[0] and mysnake[0][1] > fruit[1]:
        if mysnake_dir != 'RIGHT':
            print("4. Left")
            return 'LEFT'
        else:
            print("4. Up")
            return 'UP'

    # return check_before_self_collision(mysnake, dis_width, fruit, mysnake_dir)


def check_before_self_collision(mysnake, dis_width, fruit, mysnake_dir):
    global IS_COLLISION_DETECTED
    for block in mysnake[1:]:
        if mysnake_dir == "UP":
            diff = mysnake[0][1] - block[1]
            if 0 < diff <= 20 and mysnake[0][0] == block[0]:
                IS_COLLISION_DETECTED = True
                if mysnake[0][0] < fruit[0]:
                    if not is_snake_collision_right(mysnake, dis_width):
                        return 'RIGHT'
                    else:
                        return 'LEFT'
                else:
                    if not is_snake_collision_left(mysnake, 0):
                        return 'LEFT'
                    else:
                        return 'RIGHT'
        elif mysnake_dir == "DOWN":
            diff = block[1] - mysnake[0][1]
            if 0 < diff <= 20 and mysnake[0][0] == block[0]:
                IS_COLLISION_DETECTED = True
                if mysnake[0][0] < fruit[0]:
                    if not is_snake_collision_right(mysnake, dis_width):
                        return 'RIGHT'
                    else:
                        return 'LEFT'
                else:
                    if not is_snake_collision_left(mysnake, 0):
                        return 'LEFT'
                    else:
                        return 'RIGHT'
        elif mysnake_dir == "LEFT":
            diff = mysnake[0][0] - block[0]
            if 0 < diff <= 20 and mysnake[0][1] == block[1]:
                IS_COLLISION_DETECTED = True
                if mysnake[0][1] < fruit[1]:
                    if not is_snake_collision_down(mysnake, dis_width):
                        return 'DOWN'
                    else:
                        return 'UP'
                else:
                    if not is_snake_collision_up(mysnake, 0):
                        return 'UP'
                    else:
                        return 'DOWN'
        elif mysnake_dir == "RIGHT":
            diff = block[0] - mysnake[0][0]
            if 0 < diff <= 20 and mysnake[0][1] == block[1]:
                IS_COLLISION_DETECTED = True
                if mysnake[0][1] < fruit[1]:
                    if not is_snake_collision_down(mysnake, dis_width):
                        return 'DOWN'
                    else:
                        return 'UP'
                else:
                    if not is_snake_collision_up(mysnake, 0):
                        return 'UP'
                    else:
                        return 'DOWN'


def is_snake_collision_right(mysnake, dis_width):
    my_x_pos = int(mysnake[0][0])
    my_y_pos = int(mysnake[0][1])
    while my_x_pos < dis_width:
        for block in mysnake[1:]:
            if block[0] == my_x_pos and block[1] == my_y_pos:
                return True
        my_x_pos += 1
    return False


def is_snake_collision_left(mysnake, limit):
    my_x_pos = int(mysnake[0][0])
    my_y_pos = int(mysnake[0][1])
    while my_x_pos > 0:
        for block in mysnake[1:]:
            if block[0] == my_x_pos and block[1] == my_y_pos:
                return True
        my_x_pos -= 1
    return False


def is_snake_collision_up(mysnake, limit):
    my_x_pos = int(mysnake[0][0])
    my_y_pos = int(mysnake[0][1])
    while my_y_pos > limit:
        for block in mysnake[1:]:
            if block[1] == my_y_pos and block[0] == my_x_pos:
                return True
        my_y_pos -= 1
    return False


def is_snake_collision_down(mysnake, dis_width):
    my_x_pos = int(mysnake[0][0])
    my_y_pos = int(mysnake[0][1])
    while my_y_pos < dis_width:
        for block in mysnake[1:]:
            if block[1] == my_y_pos and block[0] == my_x_pos:
                return True
        my_y_pos += 1
    return False


def check_other_snake_collision(mysnake, othersnake, dis_width, fruit, mysnake_dir):
    global IS_OTHERSNAKE_COLLISION_DETECTED
    for block in othersnake:
        if mysnake_dir == "UP":
            diff = mysnake[0][1] - block[1]
            if 0 < diff <= 20 and mysnake[0][0] == block[0]:
                IS_OTHERSNAKE_COLLISION_DETECTED = True
                if mysnake[0][0] < fruit[0]:
                    if not is_othersnake_collision_right(mysnake, othersnake, dis_width):
                        return 'RIGHT'
                    else:
                        return 'LEFT'
                else:
                    print("left")
                    if not is_othersnake_collision_left(mysnake, othersnake):
                        return 'LEFT'
                    else:
                        return 'RIGHT'
        elif mysnake_dir == "DOWN":
            diff = block[1] - mysnake[0][1]
            if 0 < diff <= 20 and mysnake[0][0] == block[0]:
                IS_OTHERSNAKE_COLLISION_DETECTED = True
                if mysnake[0][0] < fruit[0]:
                    if not is_othersnake_collision_right(mysnake, othersnake, dis_width):
                        return 'RIGHT'
                    else:
                        return 'LEFT'
                else:
                    if not is_othersnake_collision_left(mysnake, othersnake):
                        return 'LEFT'
                    else:
                        return 'RIGHT'
        elif mysnake_dir == "LEFT":
            diff = mysnake[0][0] - block[0]
            if 0 < diff <= 20 and mysnake[0][1] == block[1]:
                IS_OTHERSNAKE_COLLISION_DETECTED = True
                if mysnake[0][1] < fruit[1]:
                    if not is_othersnake_collision_down(mysnake, othersnake, dis_width):
                        return 'DOWN'
                    else:
                        return 'UP'
                else:
                    if not is_othersnake_collision_up(mysnake, othersnake):
                        return 'UP'
                    else:
                        return 'DOWN'
        elif mysnake_dir == "RIGHT":
            diff = block[0] - mysnake[0][0]
            if 0 < diff <= 20 and mysnake[0][1] == block[1]:
                IS_OTHERSNAKE_COLLISION_DETECTED = True
                if mysnake[0][1] < fruit[1]:
                    if not is_othersnake_collision_down(mysnake, othersnake, dis_width):
                        return 'DOWN'
                    else:
                        return 'UP'
                else:
                    if not is_othersnake_collision_up(mysnake, othersnake):
                        return 'UP'
                    else:
                        return 'DOWN'


def is_othersnake_collision_right(mysnake, othersnake, dis_width):
    my_x_pos = int(mysnake[0][0])
    my_y_pos = int(mysnake[0][1])
    while my_x_pos < dis_width:
        for block in othersnake[1:]:
            if block[0] == my_x_pos and block[1] == my_y_pos:
                return True
        my_x_pos += 1
    return False


def is_othersnake_collision_left(mysnake, othersnake):
    my_x_pos = int(mysnake[0][0])
    my_y_pos = int(mysnake[0][1])
    while my_x_pos > 0:
        for block in othersnake[1:]:
            if block[0] == my_x_pos and block[1] == my_y_pos:
                return True
        my_x_pos -= 1
    return False


def is_othersnake_collision_up(mysnake, othersnake):
    my_x_pos = int(mysnake[0][0])
    my_y_pos = int(mysnake[0][1])
    while my_y_pos > 0:
        for block in othersnake[1:]:
            if block[1] == my_y_pos and block[0] == my_x_pos:
                return True
        my_y_pos -= 1
    return False


def is_othersnake_collision_down(mysnake, othersnake, dis_width):
    my_x_pos = int(mysnake[0][0])
    my_y_pos = int(mysnake[0][1])
    while my_y_pos < dis_width:
        for block in othersnake[1:]:
            if block[1] == my_y_pos and block[0] == my_x_pos:
                return True
        my_y_pos += 1
    return False


def get_direction(mysnake, othersnake, dis_width, fruit, mysnake_dir):
    my_direction = check_before_self_collision(mysnake, dis_width, fruit, mysnake_dir)
    if my_direction is None:
        my_direction = check_other_snake_collision(mysnake, othersnake, dis_width, fruit, mysnake_dir)
        if my_direction is None:
            if IS_COLLISION_DETECTED:
                my_direction = change_dir_if_collision_detected(mysnake, mysnake_dir, dis_width)
            elif IS_OTHERSNAKE_COLLISION_DETECTED:
                my_direction = change_dir_if_othersnake_collision_detected(mysnake,othersnake, mysnake_dir, dis_width)
            else:
                my_direction = change_auto_direction(mysnake, fruit, mysnake_dir, dis_width)

    return my_direction


def change_dir_if_collision_detected(mysnake, mysnake_dir, dis_width):
    global IS_COLLISION_DETECTED

    limit1 = mysnake[0][1] - 40
    if limit1 < 0:
        limit1 = 0
    limit2 = mysnake[0][1] + 40
    if limit2 > dis_width:
        limit2 = dis_width
    if mysnake_dir == "LEFT":
        is_collision_up = is_snake_collision_up(mysnake, limit1)
        is_collision_down = is_snake_collision_down(mysnake, limit2)

        if is_collision_up or is_collision_down:
            return "LEFT"
        else:
            IS_COLLISION_DETECTED = False
            return "LEFT"
    if mysnake_dir == "RIGHT":
        is_collision_up = is_snake_collision_up(mysnake, limit1)
        is_collision_down = is_snake_collision_down(mysnake, limit2)

        if is_collision_up or is_collision_down:
            return "RIGHT"
        else:
            IS_COLLISION_DETECTED = False
            return "RIGHT"
    if mysnake_dir == "UP":
        is_collision_left = is_snake_collision_left(mysnake, limit1)
        is_collision_right = is_snake_collision_right(mysnake, limit2)

        if is_collision_left or is_collision_right:
            return "UP"
        else:
            IS_COLLISION_DETECTED = False
            return "UP"
    if mysnake_dir == "DOWN":
        is_collision_left = is_snake_collision_left(mysnake, limit1)
        is_collision_right = is_snake_collision_right(mysnake, limit2)

        if is_collision_left or is_collision_right:
            return "DOWN"
        else:
            IS_COLLISION_DETECTED = False
            return "DOWN"


def change_dir_if_othersnake_collision_detected(mysnake, othersnake, mysnake_dir, dis_width):
    global IS_OTHERSNAKE_COLLISION_DETECTED

    # limit1 = mysnake[0][1] - 40
    limit1 = othersnake[0][1] - 40
    if limit1 < 0:
        limit1 = 0
    # limit2 = mysnake[0][1] + 40
    limit2 = othersnake[0][1] - 40
    if limit2 > dis_width:
        limit2 = dis_width
    if mysnake_dir == "LEFT":
        is_collision_up = is_othersnake_collision_up(mysnake,othersnake)
        is_collision_down = is_othersnake_collision_down(mysnake,othersnake,limit2)

        if is_collision_up or is_collision_down:
            return "LEFT"
        else:
            IS_OTHERSNAKE_COLLISION_DETECTED = False
            return "LEFT"
    if mysnake_dir == "RIGHT":
        is_collision_up = is_othersnake_collision_up(mysnake,othersnake)
        is_collision_down = is_othersnake_collision_down(mysnake,othersnake,limit2)

        if is_collision_up or is_collision_down:
            return "RIGHT"
        else:
            IS_OTHERSNAKE_COLLISION_DETECTED = False
            return "RIGHT"
    if mysnake_dir == "UP":
        is_collision_left = is_othersnake_collision_left(mysnake,othersnake)
        is_collision_right = is_othersnake_collision_right(mysnake,othersnake,limit2)

        if is_collision_left or is_collision_right:
            return "UP"
        else:
            IS_OTHERSNAKE_COLLISION_DETECTED = False
            return "UP"
    if mysnake_dir == "DOWN":
        is_collision_left = is_othersnake_collision_left(mysnake,othersnake)
        is_collision_right = is_othersnake_collision_right(mysnake,othersnake,limit2)

        if is_collision_left or is_collision_right:
            return "DOWN"
        else:
            IS_OTHERSNAKE_COLLISION_DETECTED = False
            return "DOWN"            

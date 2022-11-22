import math

# Custom utility for Pungi:
##direction algorithm here ##
# conpute decision scores for each direction
#  if we have won points this round:
#  Score =
#   Distance to apple*2 (- distance to original point )
#   (- (Distance to all self body points / number of body_points) * 0.5)
#   (- (Distance to all other snakes' body points / number of other snakes' body_points) * 0.5)
#  if we havn't won points this round:
#  Score =
#   Distance to apple*2 (- distance to original point )
def compute_Decison_score(Predicted_location, fruit_position):
    location_next = Predicted_location
    die_point = [0, 0]
    if snake2_score == 0:
        Decision_Score = 2 * math.dist(location_next, fruit_position) - math.dist(
            location_next, die_point
        )

    else:
        Self_body_Penalty = 0
        Other_body_Penalty = 0
        for pos in snake2_body:
            Self_body_Penalty = Self_body_Penalty + math.dist(location_next, pos)
        for pos2 in snake1_body:
            Other_body_Penalty = Other_body_Penalty + math.dist(location_next, pos2)
        Decision_Score = (
            2 * math.dist(location_next, fruit_position)
            - math.dist(location_next, die_point)
            - 0.5 * (Self_body_Penalty / len(snake2_body))
            - 0.5 * (Other_body_Penalty / len(snake1_body))
        )

    return Decision_Score


def snake_pungi(
    mysnake,
    othersnake,
    fruit,
    mysnake_dir,
    othersnake_dir,
    mysnake_pos,
    othersnake_pos,
    window_x,
    window_y,
):
    # Pungi: Team Pungi is using snake 2
    # assuming the location for differnt directions for score computation
    move_left_position = [mysnake_pos[0] - 10, mysnake_pos[1]]
    move_right_position = [mysnake_pos[0] + 10, mysnake_pos[1]]
    move_down_position = [mysnake_pos[0], mysnake_pos[1] + 10]
    move_up_position = [mysnake_pos[0], mysnake_pos[1] - 10]

    # Compare decision scores for 3 directions, select the smallet one
    Decision_score_up = compute_Decison_score(move_up_position, fruit)
    Decision_score_down = compute_Decison_score(move_down_position, fruit)
    Decision_score_left = compute_Decison_score(move_left_position, fruit)
    Decision_score_right = compute_Decison_score(move_right_position, fruit)

    Decision = min(
        Decision_score_up,
        Decision_score_down,
        Decision_score_left,
        Decision_score_right,
    )

    ##Decision and coner case handling algorithm algorithm##
    if Decision == Decision_score_up:
        if snake2_direction != "DOWN":
            snake2_direction = "UP"
        elif snake2_direction == "DOWN":
            snake2_direction = "RIGHT"

    elif Decision == Decision_score_down:
        if snake2_direction != "UP":
            snake2_direction = "DOWN"
        elif snake2_direction == "UP":
            snake2_direction = "LEFT"

    elif Decision == Decision_score_left:
        if snake2_direction != "RIGHT":
            snake2_direction = "LEFT"
        elif snake2_direction == "RIGHT":
            snake2_direction = "UP"

    elif Decision == Decision_score_right:
        if snake2_direction != "LEFT":
            snake2_direction = "RIGHT"
        elif snake2_direction == "LEFT":
            snake2_direction = "DOWN"
    ##Check for boundaries
    if snake2_direction == "LEFT" or snake2_direction == "RIGHT":
        mysnake_new_position_x = move_left_position[0]
        if mysnake_new_position_x < 0 or mysnake_new_position_x > window_x - 10:
            snake2_direction = "UP"

    elif snake2_direction == "UP" or snake2_direction == "DOWN":
        mysnake_new_position_y = move_up_position[1]
        if mysnake_new_position_y < 0 or mysnake_new_position_y > window_y - 10:
            snake2_direction = "LEFT"
    return snake2_direction

    # to do: detect if the one step on route has body of self or opponet, if there is, change direction

def turn_right():
    for i in range(0,3):
        turn_left()
def change_direction():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
    elif wall_in_front() and wall_on_right():
        turn_left()
    
while not at_goal():
    if wall_in_front():
        change_direction()
    else:
        move()
        if right_is_clear():
            turn_right()

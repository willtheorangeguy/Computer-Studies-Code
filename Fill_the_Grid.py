def putt_balls():
    put_ball()
    move()

for i in range(80):
    putt_balls()
    if facing_east() and front_is_blocked():
        put_ball()
        turn_left()
        move()
        turn_left()
        putt_balls()
    elif facing_west() and front_is_blocked():
        put_ball()
        turn_right()
        move()
        turn_right()
        putt_balls()

putt_balls()
put_ball()

# Debug the Karel program in IDLE by replacing actuall actions with text

def facing_east():
    print("Check Karel Facing East")
    
def facing_west():
    print("Check Karel Facing West")
    
def put_ball():
    print("Karel Put a Ball")

def move():
    print("Karel Moved")

def turn_left():
    print("Karel Turned Left")

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

"""
Karel needs to take the stack of tennis balls and move it, doubling the number 
of balls.
"""

"""
Take a ball, move, then put double the amount of balls Karel took.
Precondition: Karel is on a stack of balls.
Postcondition: Karel has moved the stack and is not standing on balls.
"""
def move_and_double():
    take_ball()
    turn_around()
    move()
    put_ball()
    put_ball()
    turn_around()
    move()

"""
Move the balls from the doubling stack to the final stack.
Precondition: Karel is beside a stack of balls.
Postcondition: Karel has moved the stack and is not standing on balls.
"""
def move_balls():
    turn_around()
    move()
    while balls_present():
        take_ball()
        turn_around()
        move()
        put_ball()
        turn_around()
        move()

# When there is a stack, move and double the stack.
move()
while balls_present():
    move_and_double()

# When the stack is gone, move the doubled stack back.
if no_balls_present():
    move_balls()

# Make Karel face west.
turn_left()
turn_left()
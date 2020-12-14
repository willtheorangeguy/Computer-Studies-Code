"""
Build stacks of balls on every other column.
"""

"""
Build a stack of 3 balls the return to the starting point.
Precondition: No balls in a stack.
Postcondition: Karel is at the bottom of a stack of 3 balls.
"""
def build_a_stack():
    turn_left()
    for i in range(3):
        put_ball()
        move()
    turn_around()
    for i in range(3):
        move()
    turn_left()

# Build the first stack.
build_a_stack()

# Move and build stacks of balls only when the front is clear.
while front_is_clear():
    if front_is_clear():
        move()
        if front_is_clear():
            move()
            build_a_stack()
"""
Karel moves throughout the whole world cleaning up all the balls.
"""

"""
Moves Karel along a row, cleaning up balls if there are balls to cleanup.
Precondition: Karel is at the beginning or a dirty (or clean?) row.
Postcondition: Karel is at the end of the row and the row is clean.
"""
def row_cleanup():
    while front_is_clear():
        if balls_present():
            take_ball()
            move()
        else:
            move()

# Checks for a vertical world, to make sure we turn left beforehand.
if balls_present() and front_is_blocked():
    turn_left()
    row_cleanup()

# If not a vertical world, use the horizontal world formula as follows.            
while left_is_clear() or front_is_clear():
    row_cleanup()
    # If the front is blocked and Karel is facing east, turn left to get on to
    # the next row.
    if front_is_blocked() and facing_east() and left_is_clear():
        # Catch balls that aren't picked up.
        if balls_present():
            take_ball()
        turn_left()
        move()
        turn_left()
        row_cleanup()
    # If the front is blocked and Karel is facing west, turn right to get on to
    # the next row.
    if front_is_blocked() and facing_west() and left_is_clear():
        # Catch balls that aren't picked up.
        if balls_present():
            take_ball()
        # Send Karel back to the starting point.
        if right_is_blocked():
            turn_left()
            while front_is_clear():
                move()
            break
        turn_right()
        move()
        turn_right()
        row_cleanup()

# Catch balls that aren't picked up.
if balls_present():
    take_ball()
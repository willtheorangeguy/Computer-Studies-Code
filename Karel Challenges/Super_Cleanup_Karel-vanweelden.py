"""
Karel needs to cleanup the world, there are tennis balls randomly placed.
The world can be any size.
"""

def clean_world():
    while left_is_clear():
        clean_row()
        move_up()

"""
Precondition: Karel is at the start of a row.
Postcondition: Karel is at the end of the row, with the row cleaned.
"""
def clean_row():
    while front_is_clear():
        if balls_present():
            take_ball()
        move()
    if balls_present():
        take_ball()
    reset()
     
"""
Precondition: Karel is at the start of a row facing east. 
Postcondition: Karel is at the start of a row facing east, with the row cleaned.
"""
def reset():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

"""
Precondition: Karel is at the start of a row facing east.
Postcondition: Karel is at the next row up, facing east.
"""
def move_up():
    turn_left()
    move()
    turn_right()

clean_world()
clean_row()

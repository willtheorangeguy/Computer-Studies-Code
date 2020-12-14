"""
This program will have Karel run around the racetrack 8 times, putting a ball
on each corner.
"""

"""
Move one side of the racecourse and put down a ball at each corner.
Precondition: Karel is at a corner.
Postcondtion: Karel is at the opposite corner with a ball at said corner.
"""
def move_one_side():
    while front_is_clear():
        move()
    put_ball()
    turn_left()

# Move around the sides 32 times.
for i in range(32):
    move_one_side()
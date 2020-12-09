"""
Karel needs to be able to build a tower on every odd column, regardless of the size of the world.
"""

"""
Preconditions: Starts at floor facing east.
Postcondition: At floor facing east with tower built.
"""
def build_tower():
    turn_left()
    for i in range(3):
        put_ball()
        move()
    turn_around()
    for i in range(3):
        move()
    turn_left()

build_tower()

while front_is_clear():
    move()
    if front_is_clear():
        move()
        build_tower()

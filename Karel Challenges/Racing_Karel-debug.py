"""
This program will have Karel run around the racetrack 8 times, putting a ball
on each corner.
"""

def move():
    print("Karel moved.")

def put_ball():
    print("Karel put down a ball.")

def turn_left():
    print("Karel turned left.")

def front_is_clear():
    True
    print("Is Karel's front clear?")

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

"""
 This program has Karel paint a checkerboard
"""

def move():
    print("Karel moved.")

def turn_left():
    print("Karel turned left.")

def turn_right():
    print("Karel turned right.")

def facing_east():
    print("Is Karel facing east?")

def facing_west():
    print("Is Karel facing west?")

def front_is_blocked():
    print("Is Karel's front blocked?")

def paint_it_red():
    print("Painted square red.")

def paint_it_black():
    print("Painted square black.")

def go_back_home():
    turn_left()
    for i in range(7):
        move()
    turn_left()

for i in range(31):
    paint_it_black()
    move()
    paint_it_red()
    if facing_east() and front_is_blocked():
        paint_it_red()
        turn_left()
        move()
        turn_left()
        paint_it_red()
    elif facing_west() and front_is_blocked():
        paint_it_red()
        turn_right()
        move()
        turn_right()
        paint_it_red()
    else:
        move()
        paint_it_red()
paint_it_black()
move()
paint_it_red()
go_back_home()

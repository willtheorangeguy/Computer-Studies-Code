"""
 This program has Karel paint a checkerboard
"""
def paint_it_red():
    paint(color['red'])

def paint_it_black():
    paint(color['black'])

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
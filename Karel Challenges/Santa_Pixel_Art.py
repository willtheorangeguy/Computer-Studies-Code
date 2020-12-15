"""
Paint Santa's face in pixel art using the Karel Color command.
"""

# Moves to the bottom of Santa's face.
def move_to_outline():
    for i in range(10):
        move()
    turn_left()
    for i in range(4):
        move()
    turn_right()

# Moves back to (1,1), to reorient Karel.
# Could have made this shorter, but CodeHS crashes when we did.
def go_home():
    while not_facing_south():
        turn_left()
    if facing_south():
        while front_is_clear():
            move()
        if front_is_blocked():
            turn_right()
            while front_is_clear():
                move()
    turn_around()

# Turn left and move. (Cleans up the code a bit).
def turn_left_move():
    turn_left()
    move()

# Turn right and move. (Cleans up the code a bit).
def turn_right_move():
    turn_right()
    move()

# Move up a row in a stairclimbing-like effect.
def move_up():
    turn_left_move()
    turn_right_move()

# Move down a row in a stairclimbing-like effect.
def move_down():
    turn_left_move()
    turn_right_move()

# Paint the outline of Santa's face and hat.
def paint_outline():
    paint(color['black'])
    move()
    paint(color['black'])
    for i in range(3):
        move_up()
        paint(color['black'])
    turn_left_move()
    paint(color['black'])
    turn_right()
    move_up()
    paint(color['black'])
    turn_left()
    for i in range(3):
        move()
        paint(color['black'])
    turn_left_move()
    turn_right_move()
    for i in range(4):
        paint(color['black'])
        move()
    turn_left_move()
    paint(color['black'])
    turn_right_move()
    turn_left_move()
    for i in range(6):
        paint(color['black'])
        move()
    turn_left_move()
    paint(color['black'])
    turn_right_move()
    paint(color['black'])
    turn_left_move()
    turn_right_move()
    paint(color['black'])
    turn_left_move()
    paint(color['black'])
    move()
    turn_right_move()
    turn_left()
    paint(color['black'])
    move()
    paint(color['black'])
    turn_left()
    for i in range(3):
        move()
        paint(color['black'])
    turn_left_move()
    paint(color['black'])
    for i in range(2):
        turn_left_move()
    for i in range(4):
        move()
        paint(color['black'])
    turn_right_move()
    move()
    turn_right_move()
    for i in range(2):
        move()
        paint(color['black'])
    for i in range(2):
        turn_right_move()
    paint(color['black'])
    for i in range(3):
        move()
    turn_left_move()
    move()
    turn_right()
    paint(color['black'])
    move()
    for i in range(4):
        paint(color['black'])
        move_down()

# Paint Santa's epidermis features.
# The orange color is a little bit strange but works for these purposes.
def paint_face():
    turn_left()
    for i in range(6):
        move()
    paint(color['red'])
    turn_right()
    for i in range(3):
        move()
        paint(color['orange'])
    turn_left_move()
    turn_left()
    paint(color['orange'])
    move()
    paint(color['black'])
    for i in range(3):
        move()
        paint(color['orange'])
    move()
    paint(color['black'])
    move()
    paint(color['orange'])
    turn_left_move()
    paint(color['orange'])
    turn_left()
    for i in range(2):
        move()
        paint(color['orange'])
    move()
    turn_left()
    for i in range(2):
        move()
    turn_right()
    for i in range(2):
        move()
        paint(color['orange'])
    turn_around()
    move()
    for i in range(3):
        move()
        paint(color['orange'])

# Paint Santa's traditional Christmas hat.
def paint_hat():
    turn_left()
    for i in range(10):
        move()
    turn_right()
    for i in range(4):
        paint(color['red'])
        move()
    turn_around()
    for i in range(5):
        move()
    for i in range(3):
        paint(color['red'])
        move()
    for i in range(2):
        move()
        paint(color['red'])
    turn_right_move()
    turn_right()
    for i in range(9): # We tried to use a while not statement here, but CodeHS doesn't like it.
        move()
        paint(color['red'])
    turn_left_move()
    turn_left()
    for i in range(9): # Tried to do the same thing here but CodeHS doesn't like it here either.
        paint(color['red'])
        move()
    turn_right()
    move()
    turn_right()
    for i in range(3):
        move()
    for i in range(6): # Tried to do the same thing here but CodeHS doesn't like it here either.
        paint(color['red'])
        move()

# Pain the outline.
move_to_outline()
paint_outline()
go_home()

# Paint the face.
move_to_outline()
paint_face()
go_home()

# Paint the hat.
move_to_outline()
paint_hat()
go_home()
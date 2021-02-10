# Constants for Body
HEAD_RADIUS = 35
BODY_WIDTH = (HEAD_RADIUS * 2)
BODY_HEIGHT = 60
NUM_FEET = 3
FOOT_RADIUS = ((BODY_WIDTH) / (NUM_FEET * 2))

# Constants for Eyes
PUPIL_RADIUS = 4
PUPIL_LEFT_OFFSET = 8
PUPIL_RIGHT_OFFSET = 20
EYE_RADIUS = 10
EYE_OFFSET = 14

# Build Ghosts Function
def draw_ghost(x, y, color):
    # Head
    head = Circle(HEAD_RADIUS)
    head.set_position(x, y)
    head.set_color(color)
    add(head)
    # Body
    body = Rectangle(BODY_WIDTH, BODY_HEIGHT)
    body.set_position((x-HEAD_RADIUS), (y))
    body.set_color(color)
    add(body)
    # Feet
    for i in range(NUM_FEET):
        foot = Circle(FOOT_RADIUS)
        foot.set_position((x-FOOT_RADIUS*2), (y+BODY_HEIGHT))
        foot.set_color(color)
        add(foot)
        x = (x + FOOT_RADIUS*2) # Space out the feet
    # Eyes
    for i in range(2):
        eye = Circle(EYE_RADIUS)
        eye.set_position(((x-HEAD_RADIUS*2)-EYE_OFFSET), y)
        eye.set_color(Color.white)
        add(eye)
        x = (x + EYE_OFFSET*2) # Space out the eyes
    # Pupils
    for i in range(2):
        pupil = Circle(PUPIL_RADIUS)
        pupil.set_position(((x-HEAD_RADIUS*4)+PUPIL_LEFT_OFFSET), y)
        pupil.set_color(Color.blue)
        add(pupil)
        x = (x + EYE_OFFSET*2) # Space out the pupils

# Place Ghosts
draw_ghost(100, 75, Color.green)
draw_ghost(300, 200, Color.black)
draw_ghost(200, 250, Color.red)
draw_ghost(40, 300, Color.orange)
draw_ghost(300, 50, Color.yellow)
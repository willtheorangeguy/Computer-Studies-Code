# This program draws the CodeHS logo.
MID_X = get_width()/2
MID_Y = get_height()/2

# Create a trunk
def screen():
    # Outside frame
    r_out = Rectangle(180, 180)
    r_out.set_position((MID_X-90), (MID_Y-90))
    r_out.set_color(Color.blue)
    # Inside screen
    r_inside = Rectangle(160, 160)
    r_inside.set_position((MID_X-80), (MID_Y-80))
    r_inside.set_color(Color.white)
    # Outside stand
    c_out = Circle(20)
    c_out.set_position(MID_X, (MID_Y+100))
    c_out.set_color(Color.blue)
    # Inside stand
    c_in = Circle(15)
    c_in.set_position(MID_X, (MID_Y+100))
    c_in.set_color(Color.white)
    # Outside keyboard
    b_out = Rectangle(160, 30)
    b_out.set_position((MID_X-80), (MID_Y+100))
    b_out.set_color(Color.blue)
    # Inside keyboard
    b_in = Rectangle(140, 12)
    b_in.set_position((MID_X-70), (MID_Y+105))
    b_in.set_color(Color.white)
    # Put them on the screen
    add(r_out)
    add(r_inside)
    add(c_out)
    add(c_in)
    add(b_out)
    add(b_in)
    
# Build the logo
screen()
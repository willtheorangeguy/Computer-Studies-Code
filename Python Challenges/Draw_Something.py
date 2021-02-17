# This program draws the CodeHS logo.
MID_X = get_width()/2
MID_Y = get_height()/2

# Create the screen of the computer
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

# Create the code blocks
def blocks():
    # Top Row
    top_one = Rectangle(90, 27.5)
    top_one.set_position((MID_X-70), (MID_Y-70))
    top_one.set_color(Color.black)
    top_two = Rectangle(40, 27.5)
    top_two.set_position((MID_X+30), (MID_Y-70))
    top_two.set_color(Color.gray)
    # 1st Middle Row
    mid_one = Rectangle(32.5, 27.5)
    mid_one.set_position((MID_X-70), (MID_Y-32.5))
    mid_one.set_color(Color.black)
    mid_two = Rectangle(32.5, 27.5)
    mid_two.set_position((MID_X-27.5), (MID_Y-32.5))
    mid_two.set_color(Color.gray)
    mid_three = Rectangle(55, 27.5)
    mid_three.set_position((MID_X+15), (MID_Y-32.5))
    mid_three.set_color(Color.blue)
    # 2nd Middle Row
    mid_four = Rectangle(55, 27.5)
    mid_four.set_position((MID_X-70), (MID_Y+5))
    mid_four.set_color(Color.gray)
    mid_five = Rectangle(32.5, 27.5)
    mid_five.set_position((MID_X-5), (MID_Y+5))
    mid_five.set_color(Color.blue)
    mid_six = Rectangle(32.5, 27.5)
    mid_six.set_position((MID_X+37.5), (MID_Y+5))
    mid_six.set_color(Color.blue)
    # Bottom Row
    bot_one = Rectangle(32.5, 27.5)
    bot_one.set_position((MID_X-70), (MID_Y+42.5))
    bot_one.set_color(Color.blue)
    bot_two = Rectangle(55, 27.5)
    bot_two.set_position((MID_X-27.5), (MID_Y+42.5))
    bot_two.set_color(Color.blue)
    bot_three = Rectangle(32.5, 27.5)
    bot_three.set_position((MID_X+37.5), (MID_Y+42.5))
    bot_three.set_color(Color.blue)
    # Put them on the screen
    add(top_one)
    add(top_two)
    add(mid_one)
    add(mid_two)
    add(mid_three)
    add(mid_four)
    add(mid_five)
    add(mid_six)
    add(bot_one)
    add(bot_two)
    add(bot_three)

# Build the logo
screen()
blocks()

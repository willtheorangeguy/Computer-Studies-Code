# Tell the story of a computer that no longer works and the new one the user
# gets.

# Clear canvas, because CodeHS doesn't clear the previous scene
def clear():
    clear = Rectangle(get_width(), get_height())
    clear.set_color(Color.white)
    add(clear)

# Create a scene that looks like Vancouver
def vancouver():
    van = Rectangle(get_width(), get_height())
    van.set_color(Color.blue)
    add(van)
    words = Text("Welcome to Vancouver!")
    words.set_position((get_width()/2)-(words.get_width()/2), (get_height()/2-190))
    words.set_color(Color.green)
    words.set_font("20pt Arial")
    add(words)

# Draw home background and desk
def home_background():
    top = Rectangle(230, 30)
    top.set_position((get_width()/2)-50, (get_height()/2))
    top.set_color(Color.gray)
    add(top)
    leg1 = Rectangle(10, 200)
    leg1.set_position((get_width()/2)-40, (get_height()/2))
    leg1.set_color(Color.gray)
    add(leg1)
    leg2 = Rectangle(10, 200)
    leg2.set_position((get_width()/2)+160, (get_height()/2))
    leg2.set_color(Color.gray)
    add(leg2)

# Draw the PC and logo
def pc(x, y, logo_name, logo_color):
    screen = Rectangle(150, 120)
    screen.set_position(x, y)
    screen.set_color(Color.black)
    add(screen)
    stand = Rectangle(30, 20)
    stand.set_position(x+60, y+120)
    stand.set_color(Color.black)
    add(stand)
    logo = Text(logo_name)
    logo.set_position(x+32, y+80)
    logo.set_color(logo_color)
    logo.set_font("30pt Arial")
    add(logo)

# Draw my body and emotions
def me(x, y, mood):
    body = Line(x, y, x, (y+200))
    body.set_color(Color.black)
    add(body)
    face = Circle(44)
    face.set_position(x, y)
    face.set_color(Color.black)
    add(face)
    emotion = Circle(42)
    emotion.set_position(x, y)
    emotion.set_color(mood)
    add(emotion)
    leg1 = Line((x-35), (y+260), x, (y+200))
    leg1.set_color(Color.black)
    add(leg1)
    leg2 = Line((x+35), (y+260), x, (y+200))
    leg2.set_color(Color.black)
    add(leg2)
    arms = Line((x+50), (y+50), x, (y+80))
    arms.set_color(Color.black)
    add(arms)

# Make me able to speak
def dialog(text):
    words = Text(text)
    words.set_position((get_width()/2)-(words.get_width()/3), (get_height()/2-170))
    words.set_color(Color.black)
    words.set_font("12pt Arial")
    add(words)

# Draw the computer store, clerk and store name
def store():
    x = (get_width()/2)+60
    y = (get_height()/2)-80
    body = Line(x, y, x, (y+200))
    body.set_color(Color.black)
    add(body)
    face = Circle(44)
    face.set_position(x, y)
    face.set_color(Color.black)
    add(face)
    emotion = Circle(42)
    emotion.set_position(x, y)
    emotion.set_color(Color.white)
    add(emotion)
    arm1 = Line((x+50), (y+50), x, (y+80))
    arm1.set_color(Color.black)
    add(arm1)
    arm2 = Line((x-50), (y+50), x, (y+80))
    arm2.set_color(Color.black)
    add(arm2)
    legs1 = Line((x-35), (y+260), x, (y+200))
    legs1.set_color(Color.black)
    add(legs1)
    legs2 = Line((x+35), (y+260), x, (y+200))
    legs2.set_color(Color.black)
    add(legs2)
    top = Rectangle(230, 30)
    top.set_position((get_width()/2)-50, (get_height()/2))
    top.set_color(Color.gray)
    add(top)
    leg1 = Rectangle(10, 200)
    leg1.set_position((get_width()/2)-40, (get_height()/2))
    leg1.set_color(Color.gray)
    add(leg1)
    leg2 = Rectangle(10, 200)
    leg2.set_position((get_width()/2)+160, (get_height()/2))
    leg2.set_color(Color.gray)
    add(leg2)
    words = Text("Walnut Grove Computers")
    words.set_position((get_width()/2)-30, (get_height()/2)+20)
    words.set_color(Color.black)
    words.set_font("12pt Arial")
    add(words)

""" 
 Draws the first scene on the canvas and outputs the first
 section of text for the story.
"""
# Try to do work on my computer
def draw_scene1():
    clear()
    home_background()
    pc((get_width()/2)-15, (get_height()/2)-140, "Acer", Color.green)
    me((get_width()/2)-130, (get_height()/2)-90, Color.green)
    dialog("Let's do some homework :)")
    print("This is scene 1.")
    
""" 
 Draws the second scene on the canvas and outputs the second
 section of text for the story.
"""
# Find out my computer is not working
def draw_scene2():
    clear()
    home_background()
    pc((get_width()/2)-15, (get_height()/2)-140, "Acer", Color.red)
    me((get_width()/2)-130, (get_height()/2)-90, Color.red)
    dialog("It's not turning on!!?? :(")
    print("This is scene 2.")

""" 
 Draws the third scene on the canvas and outputs the third
 section of text for the story.
"""
# Try to get it fixed, only to find out its a ripoff
def draw_scene3():
    clear()
    store()
    me((get_width()/2)-130, (get_height()/2)-90, Color.red)
    dialog("Its going to cost $400 to fix this :(")
    print("This is scene 3.")

""" 
 Draws the fourth scene on the canvas and outputs the fourth
 section of text for the story.
"""
# Get a new, better computer in Vancouver
def draw_scene4():
    clear()
    vancouver()
    home_background()
    pc((get_width()/2)-15, (get_height()/2)-140, "Dell", Color.blue)
    me((get_width()/2)-130, (get_height()/2)-90, Color.green)
    dialog("This looks like a new computer that will work!")
    print("This is scene 4.")


#-----------------------------------------------------------
"""
 This is set up code that makes the story advance from
 scene to scene. Feel free to check out this code and
 learn how it works!
 But be careful! If you modify this code the story might
 not work anymore.
"""
scene_counter = 0

# When this function is called the next scene is drawn.
def draw_next_screen(x, y):
    global scene_counter
    scene_counter += 1

    if scene_counter == 1:
        draw_scene1()
    elif scene_counter == 2:
        draw_scene2()
    elif scene_counter == 3:
        draw_scene3()
    else:
        draw_scene4()

welcome = Text("Click to Begin!")
welcome.set_position(get_width() / 2 - welcome.get_width() / 2, get_height() / 2)
add(welcome)

add_mouse_click_handler(draw_next_screen)
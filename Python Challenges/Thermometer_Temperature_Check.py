# A simple GUI program to determine healthy body temperatures.
# Temperature Info: https://www.disabled-world.com/pics/1/body-fever-chart.png

# Get Temperature
def temp():
    global temp_c
    temp_c = float(input("What is your current body temperature? "))
    
    # Check for Farhenheit
    if temp_c > 50.0:
        global temp_c
        temp_c = ((temp_c - 32)*(5/9))
        temp_c = round(temp_c, 1)

# Run the Thermometer        
temp()

# Dimensions
CENTER_x = get_width() / 2
CENTER_y = get_height() / 2

# Build Title
title = Text("Temperature Check!")
title.set_color(Color.black)
title.set_font("30pt Arial")
title.set_position(CENTER_x - title.get_width()/2, CENTER_y - 120)
add(title)

# Build the Thermometer
ball = Circle(100)
ball.set_color(Color.gray)
ball.set_position(CENTER_x, CENTER_y)
add(ball)

# Build Temperature Reading
temp_reading = Text(str(temp_c) + " °C")
temp_reading.set_color(Color.black)
temp_reading.set_font("30pt Arial")
temp_reading.set_position(CENTER_x - temp_reading.get_width()/2, CENTER_y + temp_reading.get_height()/2)
add(temp_reading)

# Build Temperature States
def hypo(): # Hypothermia
    temp_state = Text("Hypothermia - Seek medical help!!")
    temp_state.set_color(Color.blue)
    temp_state.set_font("15pt Arial")
    temp_state.set_position(CENTER_x - temp_state.get_width()/2, CENTER_y + 130)
    add(temp_state)
    
def norm(): # Normal
    temp_state = Text("Normal - Good to go!")
    temp_state.set_color(Color.green)
    temp_state.set_font("15pt Arial")
    temp_state.set_position(CENTER_x - temp_state.get_width()/2, CENTER_y + 130)
    add(temp_state)

def fever(): # Fever
    temp_state = Text("Fever - Stay home and recuperate.")
    temp_state.set_color(Color.orange)
    temp_state.set_font("15pt Arial")
    temp_state.set_position(CENTER_x - temp_state.get_width()/2, CENTER_y + 130)
    add(temp_state)

def hyper(): # Hyperpyrexia
    temp_state = Text("Hyperpyrexia - Seek medical help!!")
    temp_state.set_color(Color.red)
    temp_state.set_font("15pt Arial")
    temp_state.set_position(CENTER_x - temp_state.get_width()/2, CENTER_y + 130)
    add(temp_state)

# Logic to Determine Ball Color and Temperature Range
# Equals  is on the worse temp, because it's better to be safe rather than sorry
if temp_c <= 35.0:
    ball.set_color(Color.blue)
    hypo()
elif temp_c > 35.0 and temp_c < 37.5:
    ball.set_color(Color.green)
    norm()
elif temp_c >= 37.5 and temp_c < 40.0:
    ball.set_color(Color.orange)
    fever()
elif temp_c >= 40.0:
    ball.set_color(Color.red)
    hyper()
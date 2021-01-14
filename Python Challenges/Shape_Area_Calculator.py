# This program is a simple area calculator for many different shapes.
# Area Calculations: https://www.omnicalculator.com/math/area

# Import the Math Module for Pi
import math

# Title Screen
print("Shape Area Calculator")
print("Can calculate the area of almost any shape in cm!")
print("Type 'help' to see a list of available shapes.")

# Ask for Shape Type
def calc():
    global type
    print("")
    type = input("What type of shape? ")

    # Logic for Input Prompt
    if type.lower() == "square":
        square()
        calc()
    elif type.lower() == "rectangle":
        rect()
        calc()
    elif type.lower() == "rect":
        rect()
        calc()
    elif type.lower() == "triangle":
        tri()
        calc()
    elif type.lower() == "tri":
        tri()
        calc()
    elif type.lower() == "circle":
        circle()
        calc()
    elif type.lower() == "ellipse":
        ellipse()
        calc()
    elif type.lower() == "trapezoid":
        trap()
        calc()
    elif type.lower() == "parallelogram":
        p_and_r()
        calc()
    elif type.lower() == "rhombus":
        p_and_r()
        calc()
    elif type.lower() == "kite":
        kite()
        calc()
    elif type.lower() == "pentagon":
        pent()
        calc()
    elif type.lower() == "hexagon":
        hex()
        calc()
    elif type.lower() == "octagon":
        oct()
        calc()
    elif type.lower() == "annulus":
        annulus()
        calc()
    elif type.lower() == "ring":
        annulus()
        calc()
    elif type.lower() == "help":
        help()
        calc()
    elif type.lower() == "quit":
        exit()
    elif type.lower() == "exit":
        exit()
    else:
        print("Sorry that shape is not supported :(")
        print("Type 'help' to see a list of available shapes.")
        calc()

# Area Calculation Functions
def square(): # Square area
    l = float(input("Side length? "))
    calc = (l*l)
    print("The area of your square is: {}cm\u00b2".format(calc))

def rect(): # Rectangle area
    l = float(input("Length? "))
    w = float(input("Width? "))
    calc = (l*w)
    print("The area of your rectangle is: {}cm\u00b2".format(calc))
    
def tri(): # Triangle area
    b = float(input("Base length? "))
    h = float(input("Height? "))
    calc = ((b*h)/2)
    print("The area of your triangle is: {}cm\u00b2".format(calc))

def circle(): # Circle area
    r = float(input("Circle radius? "))
    calc = ((math.pi*r)**2)
    print("The area of your circle is: {}cm\u00b2".format(calc))

def ellipse(): # Ellipse area
    h = float(input("Height? "))
    w = float(input("Width? "))
    calc = ((h/2)*(w/2)*(math.pi))
    print("The area of your ellipse is: {}cm\u00b2".format(calc))

def trap(): # Trapezoid area
    b = float(input("Base length? "))
    h = float(input("Height? "))
    l = float(input("Top length? "))
    calc = (((l + b) * h) / 2)
    print("The area of your trapezoid is: {}cm\u00b2".format(calc))

def p_and_r(): # Parallelogram and Rhombus area
    h = float(input("Height? "))
    b = float(input("Base length? "))
    calc = (b * h)
    print("The area of your shape is: {}cm\u00b2".format(calc))

def kite(): # Kite area
    h = float(input("Height? "))
    w = float(input("Width? "))
    calc = ((w * h)/2)
    print("The area of your kite is {}cm\u00b2".format(calc))

def pent(): # Pentagon area
    l = float(input("Side length? "))
    calc = (((l**2)*math.sqrt((25 + (10*(math.sqrt(5))))))/4)
    print("The area of your pentagon is {}cm\u00b2".format(calc))

def hex(): # Hexagon area
    l = float(input("Side length? "))
    calc = ((3/2)*(math.sqrt(3))*(l**2))
    print("The area of your hexagon is {}cm\u00b2".format(calc))

def oct(): # Octagon area
    l = float(input("Side length? "))
    calc = (2*(1+math.sqrt(2))*(l**2))
    print("The area of your octagon is {}cm\u00b2".format(calc))
    
def annulus(): # Annulus area
    in_r = float(input("Inside circle radius? "))
    out_r = float(input("Outside ring radius? "))
    if in_r > out_r:
        print("Your outside radius must be bigger than the inside radius.")
        calc()
    else:
        calc = (math.pi*((out_r**2)-(in_r**2)))
        print("The area of your annulus or ring is {}cm\u00b2".format(calc))

# Help Prompt Function
def help():
    print("Here are all the shapes available to you (case does not mattter):")
    print(" Square \n Rectangle \n Triangle \n Circle \n Ellipse \n Trapezoid \n Parallelogram \n Rhombus \n Kite \n Pentagon \
    \n Hexagon \n Octagon \n Annulus \n Ring")

# Run the Program
calc()
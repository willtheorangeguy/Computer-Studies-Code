"""
Karel needs to double the stack of tennis balls that is on second avenue.
"""

def double_stack():
    take_ball()
    move()
    for i in range(2):
        put_ball()
    move_back()

def move_back():
    turn_around()
    move()
    turn_around()
    
def move_stack():
    while balls_present():
        double_stack()

def reset();
    while balls_present():
        take_ball()
        turn_around()
        move()
        put_ball()
        turn_around()
        move()
        
def go_home():
    turn_around()
    for i in range(2):
        move()
    turn_around()
    
move()
move_stack()
move()
reset()
go_home()

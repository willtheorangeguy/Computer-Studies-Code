# Import 
from tkinter import *
from POS.menu import *
import time
window = Tk()

def main():
    # Window Heading
    window.title("POS GUI")

    # Title Bar
    version = Label(window, text = "GUI POS CREATE TASK - Version 0.1.0")
    timer = Label(window, text = (time.strftime("%H:%M:%S")))

    # GRILL Buttons
    grill1 = Button(window, text = "Bacon Cheese Burger", bg = 'orange', command = exit)
    grill2 = Button(window, text = "Ultimate Burger", bg = 'orange', command = exit)
    grill3 = Button(window, text = "Cheeseburger", bg = 'orange', command = exit)
    grill4 = Button(window, text = "Hamburger", bg = 'orange', command = exit)
    grill5 = Button(window, text = "Crispy Chicken", bg = 'orange', command = exit)
    grill6 = Button(window, text = "Chicken Wrap", bg = 'orange', command = exit)

    # CHILL Buttons
    chill1 = Button(window, text = "Mini Blizzard", bg = 'dodgerblue', command = exit)
    chill2 = Button(window, text = "Small Blizzard", bg = 'dodgerblue', command = exit)
    chill3 = Button(window, text = "Medium Blizzard", bg = 'dodgerblue', command = exit)
    chill4 = Button(window, text = "Large Blizzard", bg = 'dodgerblue', command = exit)
    chill5 = Button(window, text = "PB Parfait", bg = 'dodgerblue', command = exit)
    chill6 = Button(window, text = "Banana Split", bg = 'dodgerblue', command = exit)

    # BEVERAGE Buttons
    bev1 = Button(window, text = "Small Drink", bg = 'green', command = exit)
    bev2 = Button(window, text = "Medium Drink", bg = 'green', command = exit)
    bev3 = Button(window, text = "Large Drink", bg = 'green', command = exit)
    bev4 = Button(window, text = "Fruit Smoothie", bg = 'green', command = exit)
    bev5 = Button(window, text = "Orange Julius", bg = 'green', command = exit)
    bev6 = Button(window, text = "Banana", bg = 'green', command = exit)

    # CAKE Buttons
    cake1 = Button(window, text = "8\" Blizzard", bg = 'white', command = exit)
    cake2 = Button(window, text = "10\" Blizzard", bg = 'white', command = exit)
    cake3 = Button(window, text = "8\" Cake", bg = 'white', command = exit)
    cake4 = Button(window, text = "10\" Cake", bg = 'white', command = exit)
    cake5 = Button(window, text = "12pk Dilly Bars", bg = 'white', command = exit)
    cake6 = Button(window, text = "12pk Sandwiches", bg = 'white', command = exit)

    # Order Items
    order = Frame(window)
    items = Label(order, text = " Start an order!  \n\n\n\n\n\n\n\n\n\n\n\n\n", borderwidth = 2, relief = "groove")
    total = Label(order, text = "$ " + "0.00")
    
    # Edit Buttons
    delete = Button(window, text = "Delete Item", command = exit)
    edit = Button(window, text = "Edit Item", command = exit)
    open_food = Button(window, text = "Open Price", command = exit)
    open_disc = Button(window, text = "Open Discount", command = exit)
    payment = Button(window, text = "Take Payment", command = exit)

    # Position on Window
    version.grid(row = 1, column = 1, columnspan = 4, padx = 10)
    timer.grid(row = 1, column = 5, columnspan = 2, padx = 10)
    
    grill1.grid(row = 2, column = 1, padx = 10, pady = 5)
    grill2.grid(row = 3, column = 1, padx = 10, pady = 5)
    grill3.grid(row = 4, column = 1, padx = 10, pady = 5)
    grill4.grid(row = 5, column = 1, padx = 10, pady = 5)
    grill5.grid(row = 6, column = 1, padx = 10, pady = 5)
    grill6.grid(row = 7, column = 1, padx = 10, pady = 5)

    chill1.grid(row = 2, column = 2, padx = 10, pady = 5)
    chill2.grid(row = 3, column = 2, padx = 10, pady = 5)
    chill3.grid(row = 4, column = 2, padx = 10, pady = 5)
    chill4.grid(row = 5, column = 2, padx = 10, pady = 5)
    chill5.grid(row = 6, column = 2, padx = 10, pady = 5)
    chill6.grid(row = 7, column = 2, padx = 10, pady = 5)

    bev1.grid(row = 2, column = 3, padx = 10, pady = 5)
    bev2.grid(row = 3, column = 3, padx = 10, pady = 5)
    bev3.grid(row = 4, column = 3, padx = 10, pady = 5)
    bev4.grid(row = 5, column = 3, padx = 10, pady = 5)
    bev5.grid(row = 6, column = 3, padx = 10, pady = 5)
    bev6.grid(row = 7, column = 3, padx = 10, pady = 5)

    cake1.grid(row = 2, column = 4, padx = 10, pady = 5)
    cake2.grid(row = 3, column = 4, padx = 10, pady = 5)
    cake3.grid(row = 4, column = 4, padx = 10, pady = 5)
    cake4.grid(row = 5, column = 4, padx = 10, pady = 5)
    cake5.grid(row = 6, column = 4, padx = 10, pady = 5)
    cake6.grid(row = 7, column = 4, padx = 10, pady = 5)

    order.grid(row = 2, rowspan = 6, column = 5, columnspan = 2, padx = 10)
    items.pack(side = TOP)
    total.pack(side = BOTTOM)

    delete.grid(row = 8, column = 1, padx = 10, pady = (20, 2))
    edit.grid(row = 8, column = 2, padx = 10, pady = (20, 2))
    open_food.grid(row = 8, column = 3, padx = 10, pady = (20, 2))
    open_disc.grid(row = 8, column = 4, padx = 10, pady = (20, 2))
    payment.grid(row = 8, column = 5, padx = 10, pady = (20, 2))

    # Sustain Window
    window.mainloop()

# Build Window
main()
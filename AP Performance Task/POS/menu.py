# Holds backend functions for the POS GUI. 
# Each menu item (each button) has its own function, as well as multiple functions to make the POS system work.

# List to Hold ORDER ITEMS
order_items = []

# List to Hold PRICES
order_prices = []

# GRILL ITEMS
def bacon_cheese():
    # Item Details
    item = "Bacon Cheese Burger"
    price = 9
    # Add Item to Lists
    order_items.append(item)
    order_prices.append(price)
    # Respond
    print(item)
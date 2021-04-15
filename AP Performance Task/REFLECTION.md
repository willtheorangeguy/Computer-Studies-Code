# AP Create Performance Task Reflection

## Describe the Overall Purpose of the Program

> The purpose of this program is to present to the user a window where they can input the order items they would like to get. The user can input the order items in the form of buttons, see a list of ordered items, as well as a total, and edit the list by deleting the last item. They can also add an open price or a discount, as well as take the total and pass it off for payment processing. It can also detect when certain items are added to the order and offer coupons.

## Describe What Functionality of the Program is Demonstrated in the Video

> The video shows adding many items to the order list by clicking on the buttons. It shows asking the user if they want to use a coupon for a second cheeseburger after adding a single cheeseburger to the order menu. After items are deleted from the order list using the ‘delete item’ button. The video also shows manually adding a price to the order, as well as discounting the order. In the end, the order is completed and a window appears with the final total.

## Describe the Input and Output of the Program Demonstrated in the Video

> User input is shown through the pressing of buttons that add items to the order list. The program output is shown as the order list updates, as the list changes when items are deleted and at the end when the total of the order is taken.

## Capture Two Program Code Segments you Developed During the Administration of this Task that Contain a List Being Used to Manage Complexity in Your Program

### First Program Code Segment

``` python
# List to Hold ORDER ITEMS
order_items = []

# List to Hold PRICES
order_prices = []
```

### Second Program Code Segment, Showing how the Data in the Same List is Being Used

``` python
# Turn the Item List into a String
    num_items = len(items_list)
    item_list = ""
    for item in range(num_items):
        item_list += " "
        item_list += items_list[(item)]
        item_list += " "
        item_list += "\n"
```

## Identify the Name of the List Being Used in this Segment

> The names of the lists are ‘order_items’ and ‘order_prices’. They are referred to by different names throughout different functions, as they can be passed by parameters. For example, in the ‘total_up’ function, ‘order_items’ is referred to by the parameter ‘items_list’ and ‘order_prices’ is referred to by the parameter ‘prices’.

## Describe what the Data Contained in this List Represents in your Program

> ‘order_items’ contains a list of the names of each item the user has added to the order. These names are stored as strings. ‘order_prices’ contains the price associated with each order item. The prices are stored as either floats or integers.

## Explain how the Selected List Manages Complexity in your Program Code by Explaining why your Program Code could not be Written, or how it would be Written Differently, if you did not use the list

> The code manages complexity because it stores each item by itself in a list. This is an easier approach than a variable, as otherwise the item would be appended to a string each time, and the total would be added together as an integer. This allows the user to delete the last item and last price in the list. If the items were saved in a string, then you would have to select what part of the string to delete before deleting it. In the same way, you would have to tell the program how much you wanted to delete from the price. The list is also printed to the console every time it is interacted with, which makes it easy to see what went wrong while debugging the program.

## Capture Two Program Code Segments you Developed During the Administration of this Task that Contain a Student Developed Procedure that Implements an Algorithm and a Call to that Procedure

### Student Developed Procedure that Defines the Procedure's Name, Contains and Uses One or More Parameters and Implements and Algorithm that Contains Sequencing, Selection and Iteration

```python
# Total Up Price, Update Order List and Present User with Total
def total_up(items_list, prices):
    # Make Global Variable Available
    global items
    global total
    global meal_deal
    global total_price
    # Make Sure Meal Deal Can Only Be Redeemed Once
    if not(meal_deal):
        # Cheeseburger Meal Deal
        if "Cheeseburger" in items_list:
            # Ask to Save Money
            deal = box.askyesno("2 for $5 Deal", "Get 2 Cheeseburgers for $5?")
            # Save Money if Yes
            if deal == 1:
                items_list.append("Cheeseburger")
                prices.append(1.5)
                print(items_list)
                print(prices)
                meal_deal = True
            # Don't Save Money if No
            else:
                meal_deal = False 
        # Chicken Wrap Meal Deal
        elif "Chicken Wrap" in items_list:
            # Ask to Save Money
            deal = box.askyesno("2 for $5 Deal", "Get 2 Chicken Wraps for $5?")
            # Save Money if Yes
            if deal == 1:
                items_list.append("Chicken Wrap")
                prices.append(2)
                print(items_list)
                print(prices)
                meal_deal = True
            # Don't Save Money if No
            else:
                meal_deal = False
    # Turn the Item List into a String
    num_items = len(items_list)
    item_list = ""
    for item in range(num_items):
        item_list += " "
        item_list += items_list[(item)]
        item_list += " "
        item_list += "\n"
    # Respond & Debug
    items.configure(text = str(item_list))
    print(item_list)
    # Add Up Prices
    total_price = sum(prices)
    discount_price = (total_price*discount)
    total_price = total_price-discount_price
    # Respond & Debug
    total.configure(text = str("${:0.2f}\n".format(total_price)))
    print(total_price)
```

### Show Where the Student Developed Procedure is Being Called in the Program

```python
total_up(order_items, order_prices)
```

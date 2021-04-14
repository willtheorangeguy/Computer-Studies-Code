# AP Create Performance Task Reflection
## Describe the Overall Purpose of the Program
> The purpose of this program is to present to the user a window where they can input the order items they would like to get. The user can input the order items in the form of buttons, see a list of ordered items, as well as a total, and edit the list by deleting the last item. They can also add an open price or a discount, as well as take the total and pass it off for payment processing. It can also detect when certain items are added to the order and offer coupons.

## Describe What Functionality of the Program is Demonstrated in the Video
> The video shows adding many items to the order list through clicking on the buttons. It shows asking the user if they want to use a coupon for a second cheeseburger after adding a single cheeseburger to the order menu. After items are deleted from the order list using the ‘delete item’ button. The video also shows manually adding a price to the order, as well as discounting the order. At the end, the order is completed and a window appears with the final total. 

## Describe the Input and Output of the Program Demonstrated in the Video
> User input is shown through the pressing of buttons which add items to the order list. Program output is shown as the order list updates, as the list changes when items are deleted and at the end when the total of the order is taken. 

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
# Import
import random
import time

# Print Title
print("Play Rock Paper Scissors!\n")

# Rock Paper Scissors Game Variables
win = 0
loss = 0

# Rock Paper Scissors Game
def game():
    # Make Variables Global
    global win
    global loss
    
    # Get Selectionrock
    options = ["Rock", "Paper", "Scissors"]
    selec = random.choice(options)
    
    # Ask User for their Selection
    print("Rock..." )
    time.sleep(0.7)
    print("Paper...")
    time.sleep(0.7)
    print("Scissors...")
    time.sleep(0.7)
    print("Shoot...")
    user_selec = input("What did you shoot? ")

    # Compare User to Machine
    if user_selec.lower() == "rock" and selec.lower() == "paper":
        loss += 1
        print("\nYou lost :(")
        print("Your record is " + str(win) + " win(s) and " + str(loss) + " loss(es).\n")
        game()
    elif user_selec.lower() == "rock" and selec.lower() == "scissors":
        win += 1
        print("\nYou won!")
        print("Your record is " + str(win) + " win(s) and " + str(loss) + " loss(es).\n")
        game()
    elif user_selec.lower() == "paper" and selec.lower() == "rock":
        win += 1
        print("\nYou won!")
        print("Your record is " + str(win) + " win(s) and " + str(loss) + " loss(es).\n")
        game()
    elif user_selec.lower() == "paper" and selec.lower() == "scissors":
        loss += 1
        print("\nYou lost :(")
        print("Your record is " + str(win) + " win(s) and " + str(loss) + " loss(es).\n")
        game()
    elif user_selec.lower() == "scissors" and selec.lower() == "rock":
        loss += 1
        print("\nYou lost :(")
        print("Your record is " + str(win) + " win(s) and " + str(loss) + " loss(es).\n")
        game()
    elif user_selec.lower() == "scissors" and selec.lower() == "paper":
        win += 1
        print("\nYou won!")
        print("Your record is " + str(win) + " win(s) and " + str(loss) + " loss(es).\n")
        game()
    else:
        print("\nYou tied. Try again!")
        print("Your record is " + str(win) + " win(s) and " + str(loss) + " loss(es).\n")
        game()

game()
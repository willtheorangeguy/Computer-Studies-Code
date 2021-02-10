# Import
import random

# Get Number
num = random.randint(0, 100)

# Print Title
print("I am thinking of a random number between 1 and 100. \n")

# Guessing Game
correct = False
def guess():
   guess = int(input("Guess the number I am thinking: "))
   if guess == num:
       print("Correct! The number was " + str(num) +".\n")
       exit() # end when guess is correct
       correct = True # end when guess is correct
   elif guess > num:
       print("Too high. Try again.\n")
   elif guess < num:
       print("Too low. Try again.\n")

# Run the Game and Count Number of Attempts
attempt = 1
while guess:
    print("Guess " + str(attempt))
    attempt += 1
    guess()
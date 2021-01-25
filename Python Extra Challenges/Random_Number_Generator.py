# Import
import random

# Get Number
num = random.randint(0, 100)

# Print Title
print("I am thinking of a random number between 1 and 100.")
print("You have ten guesses. Good luck! \n")

# Guessing Game
def guess():
   guess = int(input("Guess the number I am thinking: "))
   if guess == num:
       print("Correct! The number was " + str(num) +".\n")
       exit() # end when guess is correct
   elif guess > num:
       print("Too high. Try again.\n")
   if guess < num:
       print("Too low. Try again.\n")

# Run the Game 10 Times and Count Number of Attempts
attempt = 1
for i in range(10):
    print("Guess " + str(attempt))
    attempt += 1
    guess()

# Bail User Out if They Fail
print("Sorry you did not guess in time. The number was: " + str(num) + ".")

"""
 Write a program that guesses every possible 4 digit passcode
 combinations until the correct passcode is guessed.

 The passcode is randomly generated and stored in the variable
 secretPasscode.

 Print out how many guesses it took to guess the correct passcode.
"""
import random
import itertools
import time

# Checks whether the given guess passcode is the correct passcode
def is_correct(guess_code, correct_code):
    return guess_code == correct_code

# Generates a random 4 digit passcode and returns it as a String
def generate_random_passcode():
    random_passcode = ""
    
    for i in range(4):
        random_digit = random.randint(0, 9)
        random_passcode += str(random_digit)
    return random_passcode

# Ask for password and length - for real implementation
# user_pwd = input("What is your pin? ")
# length = int(input("What is the length of your pin? "))

# CODEHS
user_pwd = generate_random_passcode()
length = len(user_pwd)

# Grab the time
start = time.time()

# Crack the password
numbers = '0123456789'
pin = ''
for num in itertools.product(numbers, repeat=length):
    password = pin.join(num)
    print(password)
    if is_correct(password, user_pwd) == True: # Stop when password is cracked
        print("Password found!")
        print("The password was: " + str(password) + ".")
        break

# Print time to run
end = time.time()
total = round((end - start), 2)
print("Crack took: " + str(total) + " seconds.")
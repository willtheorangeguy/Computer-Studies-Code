# Import Statements
import getpass # Only works in terminal
import hashlib # Kind of more secure than just hash()

# Check to See if Logged In
logged_in = False

# Ask for New Password
pwd = getpass.getpass("Enter new password: ")
hash_1 = hashlib.md5(pwd.encode()) 

# Confirm Password
while not(logged_in):
    login = getpass.getpass("Enter password: ")
    hash_2 = hashlib.md5(login.encode()) 

    # Make Sure Passwords Match
    if hash_1.hexdigest() == hash_2.hexdigest():
        print("You got it!")
        logged_in = True
        break
    else:
        print("Sorry, that did not match. Please try again.")
        continue
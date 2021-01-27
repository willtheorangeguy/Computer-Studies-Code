# Import Statements
import getpass # Only works in terminal
import hashlib # Kind of more secure than just hash()
import uuid

# Check to See if Logged In
logged_in = False

# Ask for New Password
pwd = getpass.getpass("Enter new password: ")
hash_1 = hashlib.md5().update(pwd.encode('utf8')) 

# Confirm Password
while not(logged_in):
    login = getpass.getpass("Enter password: ")
    hash_2 = hashlib.md5().update(login.encode('utf8')) 
    if str(hash_1) == str(hash_2):
        print("You got it!")
        logged_in = True
    else:
        print("Sorry, that did not match. Please try again.")
        continue



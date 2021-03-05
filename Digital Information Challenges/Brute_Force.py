import itertools
import time

# Ask for password
user_pwd = input("What is your pin? ")

# Grab the time
start = time.time()

# Crack the password
numbers = '0123456789'
pin = ''
for num in itertools.product(numbers, repeat=4):
    password = pin.join(num)
    print(password)
    if int(user_pwd) == int(password): # Stop when password is cracked
        print("Password found!")
        print("The password was: " + str(password) + ".")
        break

# Print time to run
end = time.time()
total = round((end - start), 2)
print("Crack took: " + str(total) + " seconds.")

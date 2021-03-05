import itertools
import time

# Ask for password and length
user_pwd = input("What is your pin? ")
length = int(input("What is the length of your pin? "))

# Grab the time
start = time.time()

# Crack the password
numbers = '0123456789'
pin = ''
for num in itertools.product(numbers, repeat=length):
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
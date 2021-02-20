# Make an empty list
list_of_names = []

# Ask for names and the number of names
def ask_names():
    names = int(input("How many names do you have? "))
    global list_of_names
    for i in range(names):
        i += 1
        name = input("Name " + str(i) + ": ")
        list_of_names.append(name)

# Print the names based on place
def print_names():
    global list_of_names
    first = list_of_names[0]
    list_of_names.remove(first)
    
    last = list_of_names[-1]
    list_of_names.remove(last)
    
    # Could make people with two last names have an imaginary middle name,
    # Mexican/Spanish culture is a good representation of this edge case.
    middle = str(list_of_names) 
    
    print("First name: " + str(first))
    print("Middle name(s): " + middle)
    # This checks to make sure they have a middle name, and also makes the
    # output look better, but CodeHS doesn't like it.
    #if list_of_names:
    #    print("Middle name(s): " + middle)
    print("Last name: " + str(last))

# Run
ask_names()
print_names()

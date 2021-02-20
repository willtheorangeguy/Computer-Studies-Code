# Ask for a number of full names and return in last names ASCII order
def sort_names(num):
    names = []
    for i in range(num):
        i += 1
        name = input("Full name of author " + str(i) + ": ")
        name = name.split()
        names.append(name[-1])
    names.sort()
    print(str(names))

# Run
sort_names(5)
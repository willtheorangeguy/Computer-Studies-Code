# Get the index to change
def get_index(word):
    while True:
        try:
            index = int(input("Enter an index (-1 to quit): "))
            if (index >= 0 and index < len(word)) or index == -1:
                return index
            else:
                print("Invalid Index!")
        except ValueError:
            print("Index must be an integer!")

# Get the letter to change to
def get_letter():
    while True:
        letter = input("Enter a letter: ")
        if len(letter) != 1:
            print("Must be exactly one character!")
        elif not letter.islower():
            print("Character must be lowercase!")
        else:
            return letter

# Get the word and conver to list
word = input("Enter a word: ")
word_as_list = list(word)

# Run the game
while True:
    index = get_index(word)
    if index == -1:
        break
    letter = get_letter()
    word_as_list[index] = letter
    print("".join(word_as_list))
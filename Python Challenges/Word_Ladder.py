# Make a word ladder!
def get_index():
    index = int(input("Enter an index (or -1 to quit): "))
    if index == -1:
        exit()
    if index > len(word):
        print("There are not that many letters in the word!")
        get_index()
    return index

def get_letter():
    letter = input("Enter a letter: ")
    letter = letter.lower()
    if len(letter) > 1:
        print("Must be exactly one character!")
        get_letter()
    return letter

def change_word():
    global word
    index = get_index()
    letter = get_letter()
    word[index] = letter
    new_word = "".join(word)
    print(new_word)
    change_word()
    

word = input("Enter a word: ")
word = list(word)
change_word()

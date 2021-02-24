# Return the number of words and indices that contain "owl"!
def owl_count():
    text = input("Enter some text: ")
    split_text = text.split()
    num_owls = 0
    index_owls = []
    for i, word in enumerate(split_text):
        if "owl" in word:
            num_owls += 1
            index_owls.append(i)
    print("There were " + str(num_owls) + " words that contained 'owl'.")
    print("They occured at indices: " + str(index_owls))

# Run
owl_count()

# Sample Text
# I really like owls. Did you know that an owl's eyes are more than twice as big as the eyes of other birds of comparable weight? And that when an owl partially closes its eyes during the day, it is just blocking out light? Sometimes I wish I could be an owl.
# My mom loves owls as well. She has lots of owl artwork. My dog howls at owls.
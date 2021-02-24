"""
 This program encodes user input into binary data!
 Your job is to write the textToBinary function
"""
# For every character in the text,
# convert the character into its ASCII decimal encoding
# then convert that decimal value into its equivalent binary encoding
# and combine each binary encoding to get the resulting binary string
def text_to_binary(text):
    letters = list(text)
    binary = ""
    for letter in letters:
        decimal_value = ord(letter)
        bin_value = decimal_to_binary(decimal_value)
        binary = binary + bin_value
        # Add a space to make it look pretty
        # binary += bin_value  + " "
    return binary


# Converts a given decimal value into an 8 bit binary value
def decimal_to_binary(decimal_value):
    binary_base = 2
    num_bits_desired = 8
    binary_value = str(bin(decimal_value))[2:]
    
    while len(binary_value) < num_bits_desired:
        binary_value = "0" + binary_value
    
    return binary_value

# Run
text = input("Input the string you would like to encode: ")
binary = text_to_binary(text)
print(binary)
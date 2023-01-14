'''
This is a python file to count characters in a string input given by the user
'''

# User input
text = input("Enter a text/paragraph : ")

# Make all the characters in the text input a list of unique characters
chars_unique = list(set(text))

# Sorting the characters so it will be in order
chars_unique.sort()

print("Characters in this text/paragraph")

# loop through each character in chars_unique

for char in chars_unique :
    counter = 0
    for text_chars in text :
        # character counter
        if text_chars == char :
            counter += 1
    print(f"{char} : {counter}")

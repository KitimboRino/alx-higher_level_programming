#!/usr/bin/python3

def uppercase(input_str):
    for char in input_str:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase by subtracting the ASCII difference
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print(uppercase_char, end="")
        else:
            # Print the character as is
            print(char, end="")
    
    # Print a new line after processing the entire string
    print()

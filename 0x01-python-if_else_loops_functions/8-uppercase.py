#!/usr/bin/python3

def uppercase(input_str):
    result = ""  # Initialize an empty string to store the result
    for char in input_str:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase by subtracting the ASCII difference and append to result
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            # Append the character as is to result
            result += char
    
    # Use a single print function to print the entire result followed by a new line
    print(result)

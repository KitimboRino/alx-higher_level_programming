#!/usr/bin/python3
def no_c(my_string):
    # Initialize an empty string to store the result
    new_string = ""

    # Iterate through each character in the input string
    for element in my_string:
        # Check if the character is not 'c' or 'C'
        if element.lower() != 'c':
            # Append the character to the result string
            new_string += element

    # Return the new string without 'c' and 'C'
    return new_string

#!/usr/bin/python3

def print_last_digit(number):
    # Check if the number is negative
    if number < 0:
        # If negative, calculate the last digit using the modulo operator
        # The negative sign is applied to ensure the result is negative
        last_num = (-number % 10)
    # If the number is zero or positive
    elif number >= 0:
        # Calculate the last digit using the modulo operator
        last_num = number % 10

    # Print the last digit using formatted string and prevent a newline
    print("{:d}".format(last_num), end="")

    # Return the last digit
    return (last_num)

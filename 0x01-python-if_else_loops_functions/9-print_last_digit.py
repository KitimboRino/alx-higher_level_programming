#!/usr/bin/python3

def print_last_digit(number):
    # Handle negative numbers by using abs() and take the remainder when dividing by 10
    if number < 0:
        last_num = abs(number) % 10
    else:
        # For non-negative numbers, simply take the remainder when dividing by 10
        last_num = number % 10
    
    # Print the last digit followed by a new line
    print("{:d}".format(last_num), end="")

    # Return the value of the last digit
    return last_num

#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Use "{:d}".format() to format and print the integer value
        print("{:d}".format(value))
        
        # If the formatting and printing are successful, return True
        return True
    except (ValueError, TypeError):
        # Catch ValueError (if value cannot be formatted as an integer)
        # If an exception occurs, return False
        return False

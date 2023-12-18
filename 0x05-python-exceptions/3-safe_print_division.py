#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        # Attempt to perform the division
        div = a / b
    except ZeroDivisionError:
        # Catch ZeroDivisionError if the denominator is zero
        div = None
    finally:
        # Print the result inside the finally block
        print("Inside result: {}".format(div))
        # Return the value of the division
        return div

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Check if the list is not empty
    if my_list:
        # Iterate through the list in reverse order
        for elm in my_list[::-1]:
            # Print each integer using str.format()
            print("{:d}".format(elm))

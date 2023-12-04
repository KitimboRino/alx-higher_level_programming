#!/usr/bin/python3
def max_integer(my_list=[]):
    # Check if the list is not empty
    if my_list:
        # Sort the list in reverse order
        my_list.sort(reverse=True)
        # Return the first element (maximum integer)
        return my_list[0]

    # Return None if the list is empty
    return None

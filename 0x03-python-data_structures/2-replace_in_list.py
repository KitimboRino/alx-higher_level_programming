#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # Check if idx is negative
    if idx < 0:
        # If negative, return the original list without modification
        return my_list

    # Check if idx is out of range
    if idx >= len(my_list):
        # If out of range, return the original list without modification
        return my_list

    # Replace the element at the specified index
    my_list[idx] = element

    # Return the modified list
    return my_list

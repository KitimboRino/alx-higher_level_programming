#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        # Return the original list without modification
        return my_list

    # Create a new list with the same elements as the original list
    new_list = list(my_list)

    # Replace the element at the specified index in the new list
    new_list[idx] = element

    # Return the new list with the modified element
    return new_list

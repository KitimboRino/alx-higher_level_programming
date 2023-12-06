#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to store unique integers
    unique_integers = set()

    # Iterate through the list and add unique integers to the set
    for number in my_list:
        unique_integers.add(number)

    # Sum up the unique integers
    result = sum(unique_integers)

    return result

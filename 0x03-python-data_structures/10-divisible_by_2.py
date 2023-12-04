#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Initialize an empty list to store True or False values
    result_list = []

    # Iterate through the original list
    for num in my_list:
        # Check if the integer is a multiple of 2
        result_list.append(num % 2 == 0)

    return result_list

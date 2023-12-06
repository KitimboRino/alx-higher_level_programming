#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys and print the dictionary entries
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")

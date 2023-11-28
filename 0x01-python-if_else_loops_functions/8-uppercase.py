#!/usr/bin/python3

def uppercase(input_str):
    for char in input_str:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase by subtracting the ASCII difference
            char = chr(ord(char) - ord('a') + ord('A'))
        print("{:s}".format(char), end="")
    print()

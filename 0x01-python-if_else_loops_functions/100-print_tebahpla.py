#!/usr/bin/python3

# Iterate over ASCII values from 'z' (122) to 'a' (97) in reverse order
for i in range(122, 96, -1):
    # Check if the current ASCII value corresponds to a lowercase letter
    if i % 2:
        # Convert the ASCII value to uppercase by subtracting 32
        i = i - 32
    # Print the character represented by the current ASCII value
    print("{:c}".format(i), end="")

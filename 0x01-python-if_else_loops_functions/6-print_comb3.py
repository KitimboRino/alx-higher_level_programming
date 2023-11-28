#!/usr/bin/python3

# Iterate over the tens place (i) from 0 to 8
for i in range(9):
    # Iterate over the ones place (j) from i+1 to 9
    for j in range(i + 1, 10):
        # Check if the concatenated number (i*10 + j) is less than 89
        if i * 10 + j < 89:
            # Print the concatenated number with the specified format
            print("{:d}{:d}".format(i, j), end=", ")

# Print the number 89 separately after the loop
print("{:d}".format(89))

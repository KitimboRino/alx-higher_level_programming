#!/usr/bin/python3

# Define the fizzbuzz function
def fizzbuzz():
    # Loop through numbers from 1 to 100 (inclusive)
    for i in range(1, 101):
        # Check if the number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        # Check if the number is divisible by 3
        elif i % 3 == 0:
            print("Fizz ", end="")
        # Check if the number is divisible by 5
        elif i % 5 == 0:
            print("Buzz ", end="")
        # If the number is not divisible by 3 or 5, print the number itself
        else:
            print("{:d} ".format(i), end="")

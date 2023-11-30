#!/usr/bin/python3
if __name__ == '__main__':
    a = 1
    b = 2

    # Import the add function from the add_0.py file
    from add_0 import add

    # Call the add function with the values of a and b
    result = add(a, b)

    print("{} + {} = {}".format(a, b, result))

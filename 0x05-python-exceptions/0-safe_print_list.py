#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        # Catch IndexError (if access an index beyond the length)
        # Do nothing in this case (pass)
        pass
    finally:
        # Ensure a newline is printed after the elements.
        print()
    # Return the real number of elements printed.
    return count

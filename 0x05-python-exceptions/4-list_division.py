#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # Initialize an empty list to store the division results
    n_list = []

    # Iterate through the lists up to the specified list_length
    for i in range(list_length):
        try:
            # Attempt to perform element-wise division
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            # Catch TypeError if the elements are not numbers
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            # Catch ZeroDivisionError if the denominator is zero
            print("division by 0")
            div = 0
        except IndexError:
            # Catch IndexError if either list is too short
            print("out of range")
            div = 0
        finally:
            # Append the result to the n_list regardless
            n_list.append(div)
    
    # Return the list of division results
    return n_list

def complex_delete(a_dictionary, value):
    # Iterate the dic items and delete keys with the specified value
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary

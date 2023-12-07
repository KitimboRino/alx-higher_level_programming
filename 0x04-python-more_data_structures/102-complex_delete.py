def complex_delete(a_dictionary, value):
    # Iterate the dic items and delete keys with the specified value
    for key, val in list(a_dictionary.items()):
        if val == value:
            del a_dictionary[key]
    return a_dictionary

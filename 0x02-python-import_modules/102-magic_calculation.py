#!/usr/bin/python3

def magic_calculation(a, b):
    imported_module = __import__(
        "magic_calculation_102", globals(), locals(), ["add", "sub"]
    )
    add, sub = imported_module.add, imported_module.sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)

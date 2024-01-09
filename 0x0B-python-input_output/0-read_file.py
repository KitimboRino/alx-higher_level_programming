#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        pass  # File doesn't exist

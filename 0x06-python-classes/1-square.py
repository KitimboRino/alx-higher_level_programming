#!/usr/bin/python3

class Square:
    """Define a square."""

    def __init__(self, size):
        """Initialize a new Square with a given size.

        Args:
            size: The size of the square (no type or value verification).
        """
        self.__size = size  # Private instance attribute '__size'

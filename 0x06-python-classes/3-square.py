#!/usr/bin/python3

class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Initialize a new Square with an optional size.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = 0  # Private instance attribute '__size'

        # Check if the provided size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Check if the size is less than 0
        if size < 0:
            raise ValueError("size must be >= 0")

        # Set the size if it passes the checks
        self.__size = size

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2

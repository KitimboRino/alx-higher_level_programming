#!/usr/bin/python3

class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Initialize a new Square with an optional size.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = 0  # Private instance attribute '__size'

        # Initialize the size using the property setter
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size to set.
        """
        # Check if the provided value is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Check if the size is less than 0
        if value < 0:
            raise ValueError("size must be >= 0")

        # Set the size if it passes the checks
        self.__size = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

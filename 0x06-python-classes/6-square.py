#!/usr/bin/python3

class Square:
    """Define a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with optional size and position.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.__size = 0  # Private instance attribute '__size'
        self.__position = (0, 0)  # Private instance attribute '__position'

        # Initialize the size and position using the properties setters
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position to set.
        """
        # Check if the provided value is a tuple of 2 positive integers
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        # Set the position if it passes the checks
        self.__position = value

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

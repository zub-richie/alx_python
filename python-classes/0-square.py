#!/usr/bin/python3

class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def draw(self):
        """
        Draws the square as an ASCII art representation.
        """
        for _ in range(self.__size):
            print("* " * self.__size)


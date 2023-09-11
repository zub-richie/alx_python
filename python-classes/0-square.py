#!/usr/bin/python3

class Square:
    #   This class represents a square.

    def __init__(self, size):
        # Initializes a new Square instance with a given size.

        self.__size = size

    def draw(self):
        # Draws the square as an ASCII art representation.
        
        for _ in range(self.__size):
            print("* " * self.__size)

# Create a square with size 3
        return 0
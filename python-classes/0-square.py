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

# Check if this script is being run as the main module

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
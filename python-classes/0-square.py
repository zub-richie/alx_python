#!/usr/bin/python3

class Square:
    def __init__(self, size):
        self.__size = size

    def draw(self):
        for _ in range(self.__size):
            print("* " * self.__size)

# Create a square with size 3
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

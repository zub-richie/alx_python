#!/usr/bin/python3

"""This module defines the Rectangle class."""

class Rectangle(BaseGeometry):
    
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """A class representing a rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    """A class representing a rectangle."""
    def __str__(self):
        """A class representing a rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

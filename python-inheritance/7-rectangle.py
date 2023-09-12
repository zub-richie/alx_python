#!/usr/bin/python3
"""
    This module defines the Rectangle class.
    """
class Rectangle(BaseGeometry):
    """
    This module defines the __init__ class.
    """
    def __init__(self, width, height):
        """A class representing a rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    """
    This module defines the area class.
    """
    def area(self):
        return self.__width * self.__height
    """
    This module defines the __str__ class.
    """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

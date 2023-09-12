#!/usr/bin/python3
"""
This module defines if a an instance.
"""
    
class Rectangle(BaseGeometry):
    """This is a class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    """This is a class"""
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

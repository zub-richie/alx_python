#!/usr/bin/python3
"""
This module defines if a an instance .
"""

class BaseGeometry:
    """This is a class"""
    def area(self):
        raise Exception("area() is not implemented")
    """This is a class"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

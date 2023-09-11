#!/usr/bin/python3
"""
This module defines if a an instance .
"""
def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherits from a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class

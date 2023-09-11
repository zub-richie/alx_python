#!/usr/bin/python3
"""
This module defines if a an instance is true or false .
"""
def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of the specified class."""
    return type(obj) is a_class

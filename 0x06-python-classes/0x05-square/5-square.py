#!/usr/bin/python3
"""A class the defines a Square
Private instance attribute: size
Public instance method: def area(self)
Public instance method: def my_print(self)
"""
class Square:
    """
    Defines a square
    """
    def __init__(self, size=0):
        """Initializes class attributes"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

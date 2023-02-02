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
        self.__size = size

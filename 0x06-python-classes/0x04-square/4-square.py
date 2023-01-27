#!/usr/bin/python3
#4-square.py
"""A class Square that defines a square"""


class Square:
    """Defines a class Square"""
    def __init__(self, size=0):
        """initializes class parameter
        Args:
            size (int): The size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Get/Set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value)
        """Return the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

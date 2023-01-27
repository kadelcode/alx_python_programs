#!/usr/bin/python3
#3-square.py
"""Define a class Square with a method "area"""


class Square:
    """Defines a class Square"""

    def __init__(self, __size):
        """Initializes class parameter
        Args:
            size (int): The size of the new square

        """
        if not isintance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

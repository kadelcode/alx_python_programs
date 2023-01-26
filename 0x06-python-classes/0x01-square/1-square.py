#!/usr/bin/python3
#2-square.py
"""Define a class Square."""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size (int): Size of a new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater than or equal to 0")
        self.__size = size
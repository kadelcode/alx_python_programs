#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get the current size of the square"""
        return self.__size

    @setter.size
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

#!/usr/bin/python3
""" Defines a Square class """


class Square:
    """ Represent a Square """
    def __init__(self, size=0):
        """ Initializes the class attribute
        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

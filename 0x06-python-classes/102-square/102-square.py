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

    def area(self):
        """Returns the current ara of the square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Defines the == comparison to a square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the !=comparison to a square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines the < comparison to a square"""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison to a square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines the > comparison to a square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= comparison to a square"""
        return self.area() >= other.area()

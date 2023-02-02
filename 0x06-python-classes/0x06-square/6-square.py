#!/usr/bin/python3
"""A class that defines a square
Private instance attribute: size & position
Public instance method: def area(self)
                        def my_print(self)
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes class attributes"""
        self.__size = size
        self.position = position

    def size(self):
        """Getter to retrieve data"""
        return self.__size

    def size(self, value):
        """Setter to set data"""
        self.__size = value

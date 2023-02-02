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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def position(self):
        """Get the position"""
        return self.__position

    def position(self, value):
        """Set the position"""
        self.__position = value

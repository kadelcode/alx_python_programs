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
        self.__position = position

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
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isintance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
           raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

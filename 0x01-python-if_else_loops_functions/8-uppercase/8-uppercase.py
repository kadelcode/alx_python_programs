#!/usr/bin/python3

"""
A module containing `uppercase` function
"""


def uppercase(str):
    """
    This function prints a string in uppercase
    followed by a new line.
    @str: the string to convert uppercase
    """

    # check if character in the string, is lowercase
    for c in str:
        if ((ord(c) >= 97) and (ord(c) <= 122)):
            """
            change the lowercase character to its
            corresponding uppercase character
            """
            c = chr(ord(c) - ord('a') + ord('A'))
        print(c, end="")
    print()

#!/usr/bin/python3

"""
This module contains a function
called `islower` which checks for
lowercase character
"""

def islower(c):
    """
    This function checks for lowercase character.
    @c: A character argument
    Return: It returns `True` if arg `c` is lowercase.
            Else, returns `False`.
    """

    if ((ord(c) >= 97) and (ord(c) <= 122)):
            return True
    else:
        return False

#!/usr/bin/python3

"""
A module that contains a function
named `print_last_digit`
"""


def print_last_digit(number):
    """
    A function that prints the last
    digit of a number.
    number: the number to print its last digit.
    """

    # ensure the number is non-negative
    number = abs(number)

    last_digit = number % 10  # last digit

    # print the last digit
    print(last_digit, end="")

    return last_digit

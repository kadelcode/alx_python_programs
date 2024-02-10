#!/usr/bin/python3

"""
This module contains a program that prints the
ASCII alphabet, in lowercase. All letters are
printed except `q` and `e`
"""

for num in range(97, 123):
    if ((chr(num) == 'q') or (chr(num) == 'e')):
        continue
    print(f"{chr(num)}", end="")

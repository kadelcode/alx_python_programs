#!/usr/bin/python3

"""
A module containing a program that prints
numbers from 0 to 99.
"""
for i in range(100):
    print(f'{i:02}', end=', ' if i < 99 else '\n')

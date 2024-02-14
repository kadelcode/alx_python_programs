#!/usr/bin/python3

"""
A program that prints all possible
different combinations of two digits.
"""

for i in range(9):
    for j in range(i+1, 10):
        print(f"{i}{j}", end="")
        if ((i == 8) and (j == 9)):
            print("\n")
            break
        print(",", end=" ")

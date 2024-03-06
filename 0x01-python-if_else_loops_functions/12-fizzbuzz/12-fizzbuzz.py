"""
A module that contains a function: `fizzbuzz()`
"""


def fizzbuzz():
    """
    A function that prints the numbers from 1 to
    100 separated by a space.

    Print `Fizz` for multiples of 3
    Print `Buzz` for multiples of 5
    Print `FizzBuzz` for both multiples of 3 and 5
    """

    for num in range(1, 101):
        if((num % 3 == 0) and (num % 5 == 0)):
            print("FizzBuzz", end=' ')
        elif(num % 3 == 0):
            print("Fizz", end=' ')
        elif(num % 5 == 0):
            print("Buzz", end=' ')
        else:
            print(num, end=" ")

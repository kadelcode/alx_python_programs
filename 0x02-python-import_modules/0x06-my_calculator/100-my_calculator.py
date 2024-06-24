#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    # Check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Get the arguments
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Dictionary to map operators to functions
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    # Check if the operator is valid
    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Perform the operation
    result = operations[operator](a, b)

    # Print the result
    print("{} {} {} = {}".format(a, operator, b, result)) 

#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# if the number is greater than 0
if (number > 0):
    print(f"{number} is positive", number)

# if number is equal to 0
elif (number == 0):
    print(f"{number} is zero", number)

# if number is less than 0
else:
    print(f"{number} is negative", number)

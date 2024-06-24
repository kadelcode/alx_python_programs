Write a program that imports all functions from the file ```calculator_1.py``` and handles basic operations.
- Usage: ```./100-my_calculator.py a operator b```
  - If the number of arguments is not 3, your program has to:
    - print ```Usage: ./100-my_calculator.py <a> <operator> <b>``` followed with a new line
    - exit with the value ```1```
  - ```operator``` can be:
      -  ```+``` for addition
      - ```-``` for subtraction
      - ```*``` for multiplication
      - ```/``` for division
  - If the operator is not one of the above:
    - print ```Unknown operator. Available operators: +, -, * and /``` followed with a new line
    - exit with the value ```1```
  - You can cast a and b into integers by using ```int()``` (you can assume that all arguments will be castable into integers)
  - The result should be printed like this: ```<a> <operator> <b> = <result>```, followed by a new line
- You are not allowed to use * for importing or ```__import__```
- Your code should not be executed when imported
```
guillaume@ubuntu:~/0x02$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

guillaume@ubuntu:~/0x02$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py <a> <operator> <b>
1
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
guillaume@ubuntu:~/0x02$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
guillaume@ubuntu:~/0x02$
```

This program will assign a random signed number to the variable ```number``` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable ```number```.
- You can find the source code [here](https://github.com/alx-tools/0x01.py/blob/master/1-last_digit_py)
- The variable ```number``` will store a different value every time you will run this program
- You don’t have to understand what ```import```, ```random.randint``` do. **Please do not touch this code**. This line should not change: ```number = random.randint(-10000, 10000)```
- The output of the program should be:
  - The string ```Last digit of```, followed by
  - the number, followed by
  - the string ```is```, followed by the last digit of ```number```, followed by
    - if the last digit is greater than 5: the string ```and is greater than 5```
    - if the last digit is 0: the string ```and is 0```
    - if the last digit is less than 6 and not 0: the string ```and is less than 6 and not 0```
  - followed by a new line
```
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$
```

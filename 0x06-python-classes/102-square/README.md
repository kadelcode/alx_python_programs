Write a class ```Square``` that defines a square by:
- Private instance attribute: ```size```:
	- property ```def size(self):``` to retrieve it
	- property setter ```def size(self, value):``` to set it
		- ```size``` must be a number (float or integer), otherwise raise a ```TypeError``` exception with the message 	```size must be a number```
		- if ```size``` is less than ```0```, raise a ```ValueError``` exception with the message ```size must be >= 0```
- Instantiation with ```size```: ```def __init__(self, size=0):```
- Public instance method: ```def area(self):``` that returns the current square area
- ```Square``` instance can answer to comparators: ```==```, ```!=```, ```>```, ```>=```, ```<``` and ```<=``` based on the square area
- You are not allowed to import any module
```
Score: 100.0% (Checks completed: 100.0%)
Write a class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be a number (float or integer), otherwise raise a TypeError exception with the message size must be a number
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Square instance can answer to comparators: ==, !=, >, >=, < and <= based on the square area
You are not allowed to import any module
guillaume@ubuntu:~/0x06$ cat 102-main.py
#!/usr/bin/python3
Square = __import__('102-square').Square

s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")

guillaume@ubuntu:~/0x06$ ./102-main.py
Square 5 < Square 6
Square 5 <= Square 6
Square 5 != Square 6
guillaume@ubuntu:~/0x06$
```

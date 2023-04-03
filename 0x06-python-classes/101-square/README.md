Write a class ```Square``` that defines a square by:(based on ```6-square.py```)
- Private instance attribute: ```size```:
	- property ```def size(self):``` to retrieve it
	- property setter ```def size(self, value):``` to set it:
		- ```size must be an integer, otherwise raise a ```TypeError``` exception with the message ```size must be an integer```
	- if ```size``` is less than ```0```, raise a ```ValueError``` exception with the message ```size must be >= 0```
- Private instance attribute: ```position```:
	- property ```def position(self):``` to retrieve it
	- property set ```def position(self, value):``` to set it:
		- ```position``` must be a tuple of 2 positive integers, otherwise raise a ```TypeError``` exception with the message ```position must be a tuple of 2 positive integer```
- Instantiation with optional ```size``` and optional ```position```: ```def __init__(self, size=0, position=(0, 0)):```
- Public instance method: ```def area(self):``` that returns the current square area
- Public instance method: ```def my_print(self):``` that prints in stdout the square with the character ```#```:
	- if ```size``` is equal to 0, print an empty line
	- ```position``` should be use by using space
- Printing a ```Square``` instance should have the same behavior as ```my_print()```
- You are not allowed to import any module
```
guillaume@ubuntu:~/0x06$ cat 101-main.py
#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)

guillaume@ubuntu:~/0x06$ ./101-main.py | tr " " "_" | cat -e
#####$
#####$
#####$
#####$
#####$
--$
$
____#####$
____#####$
____#####$
____#####$
____#####$
guillaume@ubuntu:~/0x06$
```

Write a function that checks for lowercase character.
- Prototype: ```def islower(c):```
- Returns ```True``` if c is lowercase
- Returns ```False``` otherwise
- You are not allowed to import any module
- You are not allowed to use ```str.upper()``` and ```str.isupper()```
- [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
  
You don’t need to understand ```__import__```
```
guillaume@ubuntu:~/0x01$ cat 7-main.py
#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

guillaume@ubuntu:~/0x01$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
guillaume@ubuntu:~/0x01$
```

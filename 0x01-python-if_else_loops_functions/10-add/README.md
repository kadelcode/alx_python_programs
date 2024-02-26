Write a function that adds two integers and returns the result.
Prototype: ```def add(a, b):```
Returns the value of ```a + b```
You are not allowed to import any module
You don’t need to understand ```__import__```
```
guillaume@ubuntu:~/0x01$ cat 10-main.py
#!/usr/bin/env python3
add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

guillaume@ubuntu:~/0x01$ ./10-main.py
3
98
98
guillaume@ubuntu:~/0x01$
```

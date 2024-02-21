Write a function that prints a string in uppercase followed by a new line.
- Prototype: ```def uppercase(str):```
- You can only use no more than 2 print functions with string format
- You can only use one loop in your code
- You are not allowed to import any module
- You are not allowed to use str.upper() and str.isupper()

[Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)

You don’t need to understand ```__import__```
```
guillaume@ubuntu:~/0x01$ cat 8-main.py
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")

guillaume@ubuntu:~/0x01$ ./8-main.py
BEST
BEST SCHOOL 98 BATTERY STREET
guillaume@ubuntu:~/0x01$
```

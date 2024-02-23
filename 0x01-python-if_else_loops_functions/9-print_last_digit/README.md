Write a function that prints the last digit of a number
- Prototype: ```def print_last_digit(number):```
- Returns the value of the last digit
- You are not allowed to import any module
- You don’t need to understand ```__import__```
```
guillaume@ubuntu:~/0x01$ cat 9-main.py
#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

guillaume@ubuntu:~/0x01$ ./9-main.py
8044
guillaume@ubuntu:~/0x01$
```

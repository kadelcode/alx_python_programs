-	A program that import the function _def add(a,b):_ from the file _add_0.py_ and prints the result of the addition *1 + 2 = 3*
	-	You have to use _print_ function with string format to display integers
	-	You have to assign:
		-	The value _1_ to a variable called _a_
		-	The value _2_ to a variable called _b_
		-	And use those two variables as arguments when calling the functions _add_ and _print_
	-	*a* and *b* must be defined in 2 different lines: _a = 1_ and another _b = 2_
	-	Your program should print: *<a value> + <b value> = <add(a, b) value>* followed with a new line
	-	You can only use the word _add_0_ once in your code
	-	You are not allowed to use _*_ for import or __import__
	-	Your code should not be executed when imported - by using __import__
```
guillaume@ubuntu:~/0x02$ cat add_0.py
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

guillaume@ubuntu:~/0x02$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/0x02$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/0x02$ python3 0-import_add.py 
guillaume@ubuntu:~/0x02$
```

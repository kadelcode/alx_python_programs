Write a Python script that prints exactly ```and that piece of art is useful - Dora Korpar, 2015-10-19```, followed by a new line.
- Use the function ```write``` from the ```sys``` module
- You are not allowed to use ```print```
- Your script should print to ```stderr```
- Your script should exit with the status code ```1```
```
guillaume@ubuntu:~/py/0x00$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$ echo $?
1
guillaume@ubuntu:~/py/0x00$ ./100-write.py 2> q
guillaume@ubuntu:~/py/0x00$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
guillaume@ubuntu:~/py/0x00$
```

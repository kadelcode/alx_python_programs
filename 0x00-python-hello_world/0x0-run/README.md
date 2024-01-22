### *0-run*: 
	- A Shell script that runs a Python script
	- The Python file name is saved in the environment variable _$PYFILE_
```
 guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 
```
### *0-main.py*: 
	- Python file to be executed by the Shell script

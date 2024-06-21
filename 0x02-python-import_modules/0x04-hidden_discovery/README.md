### 4-hidden_discovery.py
Write a program that prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/holbertonschool/0x02.py/raw/maste/hidden_4.pyc) (please download it locally).
-	You should print one name per line, in alpha order
-	You should print only names that do not start with ```__```
-	Your code should not be executed when imported
-	Make sure you are running your code in Python3.8.x(```hidden_4.pyc``` has been compiled with this version)
```
guillaume@ubuntu:~/0x02$ curl -Lso "hidden_4.pyc" "https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc"
guillaume@ubuntu:~/0x02$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
guillaume@ubuntu:~/0x02$
```

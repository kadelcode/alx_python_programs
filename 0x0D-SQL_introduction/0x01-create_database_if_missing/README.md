Write a script that creates the database ```hbtn_0c_0``` in your MySQL server.
- If the database ```hbtn_0c_0 already exists, your script should not fail
- You are not allowed to use the ```SELECT``` or ```SHOW``` statements
```
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$
```

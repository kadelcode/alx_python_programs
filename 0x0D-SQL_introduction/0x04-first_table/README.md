Write a script that creates a table called ```first_table``` in the current database in your MySQL server.
- ```first_table``` description:
	- ```id``` INT
	- ```name``` VARCHAR(256)
- The database name will be passed as an  argument of the ```mysql``` command
- If the table ```first_table``` already exists, your script should not fail
- You are not allowed to use the ```SELECT``` or ```SHOW``` statements
```
guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$
```

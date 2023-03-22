Write a script that prints the full description of the table ```first_table``` from the database ```hbtn_0c_0 in your MySQL server.
- The database name will be passed as an argument of the ```mysql``` command
- You are not allowed to use the ```DESCRIBE``` or ```EXPLAIN``` statements
```
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table                                                                         
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci        
guillaume@ubuntu:~/$
```

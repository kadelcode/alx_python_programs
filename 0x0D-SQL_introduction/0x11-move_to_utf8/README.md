Write a script that converts ```hbtn_0c_0``` database to UTF8(```utf8mb4```, collate ```utf8mb4_unicode_ci``` in your MySQL server.
You need to convert all of the following to ```UTF8```:
- Database ```hbtn_0c_0```
- Table ```first_table```
- Field ```name``` in ```first_table```
```
guillaume@ubuntu:~/$ cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 
Enter password: 
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
guillaume@ubuntu:~/$
```

Write a script that lists the number of records with the same score in the table ```second_table``` of the db ```hbtn_0c_0``` in your MySQL server.
- The result should display:
	- the ```score```
	- the number of records for this ```score``` with the label ```number```
- The list should be sorted by the number of records (descending)
- The database name will be passed as an argument to the ```mysql``` command
```
guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
guillaume@ubuntu:~/$
```

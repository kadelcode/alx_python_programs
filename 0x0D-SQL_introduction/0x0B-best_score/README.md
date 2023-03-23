Write a script that lists all records with a ```score >= 10``` in the table ```second_table``` of the db ```hbtn_0c_0``` in your MySQL server.
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the ```mysql``` command
```
guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
guillaume@ubuntu:~/$
```

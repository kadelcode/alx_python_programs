Write a script that updates the score of Bob to `10` in the table `second_table`.
- You are not allowed to use Bob's id value, only the ```name``` field
- The database name will be passed as an argument of the `mysql` command
```
guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$
```

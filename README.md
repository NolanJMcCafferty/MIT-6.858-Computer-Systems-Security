# Lab 1: Buffer Overflows

This is the first lab from the MIT 6.858 Computer Systems Security class which is available for free on [MIT OpenCourseWare](https://ocw.mit.edu/courses/6-858-computer-systems-security-fall-2014/).
I followed this online course independently and completed the labs on my own VM.

[Lab 1 Instructions](https://css.csail.mit.edu/6.858/2020/labs/lab1.html)

I created the exploits for this lab in: `exploit-2.py`, `exploit-3.py`, and `explout-4.py`. For the final part I fixed the server in `http.c` to protect against these exploits.

Use the following commands to run the test suite:

```$xslt
$ git clone https://github.com/NolanJMcCafferty/MIT-6.858-Computer-Systems-Security.git
$ git checkout lab1
$ make check
$ make check-fixed
```

Test Results:

```$xslt
student@6858-v20:~/lab$ make check
./check_zoobar.py
+ removing zoobar db
+ running make.. output in /tmp/make.out
+ running zookd in the background.. output in /tmp/zookd.out
PASS Zoobar app functionality
./check-bin.sh
tar xf bin.tar.gz
./check-part2.sh zookd-exstack ./exploit-2.py
./check-part2.sh: line 8: 25245 Terminated              strace -f -e none -o "$STRACELOG" ./clean-env.sh ./$1 8080 &> /dev/null
25259 --- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x7ffffffff000} ---
25259 +++ killed by SIGSEGV (core dumped) +++
25248 --- SIGCHLD {si_signo=SIGCHLD, si_code=CLD_DUMPED, si_pid=25259, si_uid=1000, si_status=SIGSEGV, si_utime=0, si_stime=1} ---
PASS ./exploit-2.py
./check-bin.sh
tar xf bin.tar.gz
./check-part3.sh zookd-exstack ./exploit-3.py
PASS ./exploit-3.py
./check-bin.sh
tar xf bin.tar.gz
./check-part3.sh zookd-nxstack ./exploit-4.py
PASS ./exploit-4.py
```

(check-fixed tests are supposed to FAIL, which indicates that the vulnerabilties have been mitigated)

```$xslt
student@6858-v20:~/lab$ make check-fixed
rm -f *.o *.pyc *.bin zookd zookd-exstack zookd-nxstack zookd-withssp shellcode.bin run-shellcode
cc zookd.c -c -o zookd.o -m64 -g -std=c99 -Wall -D_GNU_SOURCE -static -fno-stack-protector
cc http.c -c -o http.o -m64 -g -std=c99 -Wall -D_GNU_SOURCE -static -fno-stack-protector
cc -m64  zookd.o http.o   -o zookd
cc -m64 zookd.o http.o   -o zookd-exstack -z execstack
cc -m64 zookd.o http.o   -o zookd-nxstack
cc zookd.c -c -o zookd-withssp.o -m64 -g -std=c99 -Wall -D_GNU_SOURCE -static
cc http.c -c -o http-withssp.o -m64 -g -std=c99 -Wall -D_GNU_SOURCE -static
cc -m64  zookd-withssp.o http-withssp.o   -o zookd-withssp
cc -m64   -c -o shellcode.o shellcode.S
objcopy -S -O binary -j .text shellcode.o shellcode.bin
cc run-shellcode.c -c -o run-shellcode.o -m64 -g -std=c99 -Wall -D_GNU_SOURCE -static -fno-stack-protector
cc -m64  run-shellcode.o   -o run-shellcode
./check-part2.sh zookd-exstack ./exploit-2.py
./check-part2.sh: line 8: 25362 Terminated              strace -f -e none -o "$STRACELOG" ./clean-env.sh ./$1 8080 &> /dev/null
FAIL ./exploit-2.py
./check-part3.sh zookd-exstack ./exploit-3.py
FAIL ./exploit-3.py
./check-part3.sh zookd-nxstack ./exploit-4.py
FAIL ./exploit-4.py
rm shellcode.o
```

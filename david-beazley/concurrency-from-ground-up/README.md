```python
In [1]: import time

In [2]: from fib import fib

In [3]: %time fib(1)
CPU times: user 5 µs, sys: 0 ns, total: 5 µs
Wall time: 7.39 µs
Out[3]: 1

In [4]: %time fib(2)
CPU times: user 4 µs, sys: 0 ns, total: 4 µs
Wall time: 6.91 µs
Out[4]: 1

In [5]: %time fib(3)
CPU times: user 9 µs, sys: 0 ns, total: 9 µs
Wall time: 15.7 µs
Out[5]: 2

In [6]: %time fib(10)
CPU times: user 20 µs, sys: 1 µs, total: 21 µs
Wall time: 23.8 µs
Out[6]: 55

In [7]: %time fib(20)
CPU times: user 3.15 ms, sys: 0 ns, total: 3.15 ms
Wall time: 3.17 ms
Out[7]: 6765

In [8]: %time fib(30)
CPU times: user 177 ms, sys: 134 µs, total: 177 ms
Wall time: 177 ms
Out[8]: 832040

In [9]: %time fib(35)
CPU times: user 1.99 s, sys: 50 µs, total: 1.99 s
Wall time: 2 s
Out[9]: 9227465

In [10]:




```




### <code>server.py</code>
```bash
In [11]: %run server.py
Connection ('127.0.0.1', 41228)

[phunc20@denjiro-x220 concurrency-from-ground-up]$ nc localhost 25000
10
55
3
2
4
3
5
5
6
8
20
6765
30
832040
^C[phunc20@denjiro-x220 concurrency-from-ground-up]$

In [11]: %run server.py
Connection ('127.0.0.1', 41228)
Closed
```
But if you run <b>two clients</b> to request, the <b>2nd</b> one will <b>never get responce</b>.
```bash
(tf2.3.0-py3.8) [phunc20@denjiro-x220 concurrency-from-ground-up]$ tty
/dev/pts/13
(tf2.3.0-py3.8) [phunc20@denjiro-x220 concurrency-from-ground-up]$ python server.py
Connection ('127.0.0.1', 44210)


# 1st client: get instantaneous responce
[phunc20@denjiro-x220 concurrency-from-ground-up]$ tty
/dev/pts/14
[phunc20@denjiro-x220 concurrency-from-ground-up]$ nc localhost 25000
1
1
2
1
3
2
4
3

# 2nd client: wait forever
[phunc20@denjiro-x220 concurrency-from-ground-up]$ nc localhost 25000
2

# Now stop the 1st client
^C[phunc20@denjiro-x220 concurrency-from-ground-up]$ tty
/dev/pts/14

# The 2nd client then gets to speak
[phunc20@denjiro-x220 concurrency-from-ground-up]$ nc localhost 25000
2
1
3
2
10
^C
[phunc20@denjiro-x220 concurrency-from-ground-up]$ tty
/dev/pts/15

(tf2.3.0-py3.8) [phunc20@denjiro-x220 concurrency-from-ground-up]$ python server.py
Connection ('127.0.0.1', 44210)
Closed
Connection ('127.0.0.1', 44212)
Closed
^CTraceback (most recent call last):
  File "server.py", line 28, in <module>
    fib_server(('', 25000))  # on port 25000
  File "server.py", line 13, in fib_server
    client, addr = sock.accept()
  File "/usr/lib/python3.8/socket.py", line 292, in accept
    fd, addr = self._accept()
KeyboardInterrupt
```


### <code>threaded_server.py</code>
Now two clients <b>can request at the same time</b>.
```bash
(tf2.3.0-py3.8) [phunc20@denjiro-x220 concurrency-from-ground-up]$ python threaded_server.py
[phunc20@denjiro-x220 concurrency-from-ground-up]$ nc localhost 25000
1
1
2
1
3
2
4
3
5
5
6
8
7
13
[phunc20@denjiro-x220 concurrency-from-ground-up]$ nc localhost 25000
1
1
2
1
3
2
4
3
5
5
(tf2.3.0-py3.8) [phunc20@denjiro-x220 concurrency-from-ground-up]$ python threaded_server.py
Connection ('127.0.0.1', 44396)
Connection ('127.0.0.1', 44398)
^CTraceback (most recent call last):
  File "threaded_server.py", line 29, in <module>
    fib_server(('', 25000))  # on port 25000
  File "threaded_server.py", line 14, in fib_server
    client, addr = sock.accept()
  File "/usr/lib/python3.8/socket.py", line 292, in accept
    fd, addr = self._accept()
KeyboardInterrupt

(tf2.3.0-py3.8) [phunc20@denjiro-x220 concurrency-from-ground-up]$

```


### <code>dabeaz_server.py</code>
This script is from Mr. Beazley's github. It also allows two clients to run at the same time.
> The diff btw it and <code>threaded_server.py</code> is that it uses <code>pool</code> and I haven't spent time getting to know the mechanism of it.


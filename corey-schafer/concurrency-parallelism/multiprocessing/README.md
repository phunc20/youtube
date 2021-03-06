## <code>03_still_incorrect.py</code>
<pre>
(py3.8) [phunc20@artichaut-X220 multiprocessing]$ time python 03_still_incorrect.py
Master finished in 0.01(s)
Sleep for 1(s) ...
Sleep for 1(s) ...
Done sleeping 1(s) ...
Done sleeping 1(s) ...

real    0m1.068s
user    0m0.051s
sys     0m0.019s
(py3.8) [phunc20@artichaut-X220 multiprocessing]$ time python 03_still_incorrect.py
Master finished in 0.0(s)
Sleep for 1(s) ...
Sleep for 1(s) ...
Done sleeping 1(s) ...
Done sleeping 1(s) ...

real    0m1.068s
user    0m0.049s
sys     0m0.022s
</pre>


## <code>04_join.py</code>
<pre>
(py3.8) [phunc20@artichaut-X220 multiprocessing]$ python 04_join.py
Sleep for 1(s) ...
Sleep for 1(s) ...
Done sleeping 1(s) ...
Done sleeping 1(s) ...
Master finished in 1.01(s)
(py3.8) [phunc20@artichaut-X220 multiprocessing]$ python 04_join.py
Sleep for 1(s) ...
Sleep for 1(s) ...
Done sleeping 1(s) ...
Done sleeping 1(s) ...
Master finished in 1.01(s)
(py3.8) [phunc20@artichaut-X220 multiprocessing]$ time python 04_join.py
Sleep for 1(s) ...
Sleep for 1(s) ...
Done sleeping 1(s) ...
Done sleeping 1(s) ...
Master finished in 1.01(s)

real    0m1.058s
user    0m0.043s
sys     0m0.017s
(py3.8) [phunc20@artichaut-X220 multiprocessing]$ time python 04_join.py
Sleep for 1(s) ...
Sleep for 1(s) ...
Done sleeping 1(s) ...
Done sleeping 1(s) ...
Master finished in 1.01(s)

real    0m1.062s
user    0m0.053s
sys     0m0.010s
(py3.8) [phunc20@artichaut-X220 multiprocessing]$
</pre>


## <code>06_wrong_again.py</code>
This script is <b>wrong</b> in that it is <b>not different</b> from <code><b>schlafen()</b></code> for <code><b>n_processes</b></code> of times <b>consequtively, in other words, sequentially</b>.


## <code>07_accept_args.py</code>
<pre>
(py3.8) [phunc20@artichaut-X220 multiprocessing]$ python 07_accept_args.py
Sleep for 1.5(s) ...
Sleep for 1.5(s) ...
Sleep for 1.5(s) ...
Sleep for 1.5(s) ...
Sleep for 1.5(s) ...
Sleep for 1.5(s) ...
Sleep for 1.5(s) ...
Done sleeping 1.5(s) ...
Done sleeping 1.5(s) ...
Done sleeping 1.5(s) ...
Done sleeping 1.5(s) ...
Done sleeping 1.5(s) ...
Done sleeping 1.5(s) ...
Done sleeping 1.5(s) ...
Master finished in 1.51(s)
(py3.8) [phunc20@artichaut-X220 multiprocessing]$ python 07_accept_args.py
Sleep for 1.5(s) ...
Sleep for 1.5(s) ...
Sleep for 1.5(s) ...
Sleep for 1.5(s) ...
Sleep for 1.5(s) ...
Sleep for 1.5(s) ...
Sleep for 1.5(s) ...
Done sleeping 1.5(s) ...
Done sleeping 1.5(s) ...
Done sleeping 1.5(s) ...
Done sleeping 1.5(s) ...
Done sleeping 1.5(s) ...
Done sleeping 1.5(s) ...
Done sleeping 1.5(s) ...
Master finished in 1.51(s)
(py3.8) [phunc20@artic
</pre>


## <code>09_concurrent_futures.py</code>
What <code>type(f1)</code>? Corey said it's a <code>Future</code> object.
<pre>
In [11]: import concurrent.futures

In [12]: def schlafen(n_sec=1):
    ...:     print(f"Sleep for {n_sec}(s) ...")
    ...:     time.sleep(n_sec)
    ...:     print(f"Done sleeping {n_sec}(s) ...")
    ...:

In [13]: with concurrent.futures.ProcessPoolExecutor() as executor:
    ...:     f1 = executor.submit(schlafen, 2.71828)
    ...:     print(type(f1))
    ...:
<class 'concurrent.futures._base.Future'>
Sleep for 2.71828(s) ...
Done sleeping 2.71828(s) ...
</pre>

<pre>
(tf2.2.0) [phunc20@artichaut-X220 multiprocessing]$ python 09_concurrent_futures.py
Sleep for 2.71828(s) ...
Sleep for 2.71828(s) ...
Done sleeping 2.71828(s) ...
Done sleeping 2.71828(s) ...
f1.result() = Done sleeping 2.71828(s) ...
f2.result() = Done sleeping 2.71828(s) ...
Master finished in 2.75(s)
</pre>


## <code>11_sleep_54321.py</code> and <code>12_as_completed.py</code>
Maybe pay attention to the order of the prints; otherwise, me neither, I don't know what these two scripts try to teach us.

Maybe just
- looping thru the list of <code><b>Future</b></code> objects will return them in the order as the list was constructed
- looping thru <code><b>as_completed()</b></code> will return the <code><b>Future</b></code> object as soon as anyone of them has completed.
<pre>
(tf2.2.0) [phunc20@artichaut-X220 multiprocessing]$ python 12_as_completed.py
Sleep for 5(s) ...
Sleep for 4(s) ...
Sleep for 3(s) ...
Sleep for 2(s) ...
Sleep for 1(s) ...
Done sleeping 2(s) ...
Done sleeping 3(s) ...
Done sleeping 1(s) ...
Done sleeping 4(s) ...
Done sleeping 5(s) ...
Master finished in 5.03(s)
(tf2.2.0) [phunc20@artichaut-X220 multiprocessing]$ python 11_sleep_54321.py
Sleep for 5(s) ...
Sleep for 4(s) ...
Sleep for 3(s) ...
Sleep for 2(s) ...
Sleep for 1(s) ...
Done sleeping 5(s) ...
Done sleeping 4(s) ...
Done sleeping 3(s) ...
Done sleeping 2(s) ...
Done sleeping 1(s) ...
Master finished in 5.03(s)
(tf2.2.0) [phunc20@artichaut-X220 multiprocessing]$ python 11_sleep_54321.py
Sleep for 5(s) ...
Sleep for 4(s) ...
Sleep for 2(s) ...
Sleep for 3(s) ...
Sleep for 1(s) ...
Done sleeping 5(s) ...
Done sleeping 4(s) ...
Done sleeping 3(s) ...
Done sleeping 2(s) ...
Done sleeping 1(s) ...
Master finished in 5.03(s)
(tf2.2.0) [phunc20@artichaut-X220 multiprocessing]$ python 12_as_completed.py
Sleep for 5(s) ...
Sleep for 4(s) ...
Sleep for 3(s) ...
Sleep for 2(s) ...
Sleep for 1(s) ...
Done sleeping 2(s) ...
Done sleeping 1(s) ...
Done sleeping 3(s) ...
Done sleeping 4(s) ...
Done sleeping 5(s) ...
Master finished in 5.03(s)
(tf2.2.0) [phunc20@artichaut-X220 multiprocessing]$ python 11_sleep_54321.py
Sleep for 5(s) ...
Sleep for 3(s) ...
Sleep for 2(s) ...
Sleep for 4(s) ...
Sleep for 1(s) ...
Done sleeping 5(s) ...
Done sleeping 4(s) ...
Done sleeping 3(s) ...
Done sleeping 2(s) ...
Done sleeping 1(s) ...
Master finished in 5.03(s)
(tf2.2.0) [phunc20@artichaut-X220 multiprocessing]$
</pre>

## <code>13_more_ps_slower.py</code>
<pre>
(tf2.2.0) [phunc20@artichaut-X220 multiprocessing]$ python 13_more_ps_slower.py
Sleep for 20(s) ...
Sleep for 19(s) ...
Sleep for 18(s) ...
Sleep for 17(s) ...
Sleep for 16(s) ...
Done sleeping 17(s) ...
Sleep for 15(s) ...
Done sleeping 18(s) ...
Sleep for 14(s) ...
Done sleeping 19(s) ...
Sleep for 13(s) ...
Done sleeping 20(s) ...
Sleep for 12(s) ...
Done sleeping 15(s) ...
Sleep for 11(s) ...
Sleep for 10(s) ...
Done sleeping 13(s) ...
Done sleeping 14(s) ...
Sleep for 9(s) ...
Done sleeping 16(s) ...
Sleep for 8(s) ...
Done sleeping 9(s) ...
Sleep for 7(s) ...
Done sleeping 10(s) ...
Sleep for 6(s) ...
Done sleeping 11(s) ...
Sleep for 5(s) ...
Done sleeping 12(s) ...
Sleep for 4(s) ...
Done sleeping 5(s) ...
Sleep for 3(s) ...
Done sleeping 8(s) ...
Sleep for 2(s) ...
Done sleeping 6(s) ...
Done sleeping 7(s) ...
Done sleeping 2(s) ...
Done sleeping 3(s) ...
Done sleeping 4(s) ...
Master finished in 54.06(s)
(tf2.2.0) [phunc20@artichaut-X220 multiprocessing]$
</pre>


## <code>14_map.py</code>
<pre>
(tf2.2.0) [phunc20@artichaut-X220 multiprocessing]$ python 14_map.py
Sleep for 5(s) ...
Sleep for 4(s) ...
Sleep for 2(s) ...
Sleep for 3(s) ...
Sleep for 1(s) ...
Done sleeping 5(s) ...
Done sleeping 4(s) ...
Done sleeping 3(s) ...
Done sleeping 2(s) ...
Done sleeping 1(s) ...
Master finished in 5.03(s)
(tf2.2.0) [phunc20@artichaut-X220 multiprocessing]$ python 14_map.py
Sleep for 5(s) ...
Sleep for 4(s) ...
Sleep for 3(s) ...
Sleep for 2(s) ...
Sleep for 1(s) ...
Done sleeping 5(s) ...
Done sleeping 4(s) ...
Done sleeping 3(s) ...
Done sleeping 2(s) ...
Done sleeping 1(s) ...
Master finished in 5.03(s)
</pre>




IO bound: threads
CPU bound: processes

```python
[phunc20@artichaut-x220 gregory-saunders]$ python 01_duet.py
Annie: Anything you can do, I can do better.
       I can do anything better than you.
Frank: No, you can't.
Annie: Yes, I can!
Frank: No, you can't.
Annie: Yes, I can!
Frank: No, you can't.
Annie: Yes, I can. Yes, I can!
[phunc20@artichaut-x220 gregory-saunders]$ python 02_generator_accepts_input.py
Traceback (most recent call last):
  File "02_generator_accepts_input.py", line 21, in <module>
    print(singer.send("rubbish"))
TypeError: can't send non-None value to a just-started generator
[phunc20@artichaut-x220 gregory-saunders]$ python 03_generator_accepts_input.py
Annie: Anything you can do, I can do better.
       I can do anything better than you.
Frank: No, you can't.
Annie: Yes, I can!
Frank: No, you can't.
Annie: Yes, I can!
Frank: No, you can't.
Annie: Yes, I can. Yes, I can!
[phunc20@artichaut-x220 gregory-saunders]$ python 04_callback.py
Annie: Anything you can do, I can do better.
       I can do anything better than you.
Frank: No, you can't.
Exception in callback annie.<locals>.defiance(<Future finished result=None>) at 04_callback.py:7
handle: <Handle annie.<locals>.defiance(<Future finished result=None>) at 04_callback.py:7>
Traceback (most recent call last):
  File "/usr/lib/python3.8/asyncio/events.py", line 81, in _run
    self._context.run(self._callback, *self._args)
TypeError: defiance() takes 0 positional arguments but 1 was given
[phunc20@artichaut-x220 gregory-saunders]$ python 05_callback.py
Annie: Anything you can do, I can do better.
       I can do anything better than you.
Frank: No, you can't.
Annie: Yes, I can!
[phunc20@artichaut-x220 gregory-saunders]$ python 06_callback_try_fix_forget.py
Annie: Anything you can do, I can do better.
       I can do anything better than you.
Frank: No, you can't.
Traceback (most recent call last):
  File "06_callback_try_fix_forget.py", line 21, in <module>
    frank(future)
  File "06_callback_try_fix_forget.py", line 15, in frank
    when_frank_is_done_future.set_result()
TypeError: set_result() takes exactly one argument (0 given)
[phunc20@artichaut-x220 gregory-saunders]$ python 07_sans_callback.py
Annie: Anything you can do, I can do better.
       I can do anything better than you.
Frank: No, you can't.
Annie: Yes, I can!
Frank: No, you can't.
Annie: Yes, I can!
Frank: No, you can't.
Annie: Yes, I can. Yes, I certainly can!
[phunc20@artichaut-x220 gregory-saunders]$ python 08_forgot_async.py
Annie: Anything you can do, I can do better.
       I can do anything better than you.
Frank: No, you can't.
Traceback (most recent call last):
  File "08_forgot_async.py", line 25, in <module>
    loop.run_until_complete(asyncio.ensure_future(annie()))
  File "/usr/lib/python3.8/asyncio/base_events.py", line 616, in run_until_complete
    return future.result()
  File "08_forgot_async.py", line 7, in annie
    await frank()
TypeError: object NoneType can't be used in 'await' expression
[phunc20@artichaut-x220 gregory-saunders]$ python 09_no_ensure_future.py
Annie: Anything you can do, I can do better.
       I can do anything better than you.
Frank: No, you can't.
Annie: Yes, I can!
Frank: No, you can't.
Annie: Yes, I can!
Frank: No, you can't.
Annie: Yes, I can. Yes, I certainly can!
```

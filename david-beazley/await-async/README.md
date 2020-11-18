## Which video?
- [https://www.youtube.com/watch?v=E-1Y4kSsAFc&t=178s](https://www.youtube.com/watch?v=E-1Y4kSsAFc&t=178s)

## Non-default packages
- In order to `from twisted.internet import reactor, protocol` just install by `pip install twisted`

## Video structure
- **`00:00:00`**: start by talking about socket programming, an application/motivation
- **`00:11:00`**: start talking about **async**, no socket any more

## `00:11:00 - 00:16:57`, `StopIteration`
```python
In [4]: async def greeting(name):
   ...:     return "Hello " + name
   ...:

In [5]: def greet(name):
   ...:     return "Hello " + name
   ...:

In [6]: greet("Beazley")
Out[6]: 'Hello Beazley'

In [7]: greeting("Beazley")
Out[7]: <coroutine object greeting at 0x7fa84ab8ee40>

In [8]: g = greeting("Beazley")

In [9]: g.send(None)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-9-70a3cd01dee6> in <module>
----> 1 g.send(None)

StopIteration: Hello Beazley

In [10]: def run(coro):                                                                                                   [57/334]
    ...:     try:
    ...:         coro.send(None)
    ...:     except StopIteration as e:
    ...:         return e.value
    ...:

In [11]: run(g)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
<ipython-input-11-0eed3bf36c9f> in <module>
----> 1 run(g)

<ipython-input-10-5d780f90dd1e> in run(coro)
      1 def run(coro):
      2     try:
----> 3         coro.send(None)
      4     except StopIteration as e:
      5         return e.value

RuntimeError: cannot reuse already awaited coroutine

In [12]: run(greeting("Huy"))
Out[12]: 'Hello Huy'

In [13]: run(greeting("Pike"))
Out[13]: 'Hello Pike'

In [14]: async def main():                                                                                                [29/334]
    ...:     print(await greeting("Guido"))
    ...:

In [15]: run(main)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-15-8f22bbbd4c21> in <module>
----> 1 run(main)

<ipython-input-10-5d780f90dd1e> in run(coro)
      1 def run(coro):
      2     try:
----> 3         coro.send(None)
      4     except StopIteration as e:
      5         return e.value

AttributeError: 'function' object has no attribute 'send'

In [16]: run(main())
Hello Guido

In [17]: type(main)
Out[17]: function

In [18]: type(main())
<ipython-input-18-93d3160360ae>:1: RuntimeWarning: coroutine 'main' was never awaited
  type(main())
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
Out[18]: coroutine

In [19]: type(greeting)
Out[19]: function

In [20]: type(greeting())
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-20-27cdcc517f0c> in <module>
----> 1 type(greeting())

TypeError: greeting() missing 1 required positional argument: 'name'

In [21]: type(greeting("Lamy"))
<ipython-input-21-4d7aedb0e171>:1: RuntimeWarning: coroutine 'greeting' was never awaited
  type(greeting("Lamy"))
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
Out[21]: coroutine

In [22]: async def main():
    ...:     names = ["Alice", "Bob", "Carl"]
    ...:     for n in names:
    ...:         print(await greeting(n))
    ...:

In [23]: run(main())
Hello Alice
Hello Bob
Hello Carl

```

## `00:16:57 - ?`, recursive fibonacci numbers with `async`



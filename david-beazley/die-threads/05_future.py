import threading
from concurrent.futures import Future

def spam(x, y, fut):
    result = x + y
    fut.set_result(result)

fut = Future()
t = threading.Thread(target=spam, args=(1,2,fut))
t.start()
t.join()
print("Result:", fut.result())

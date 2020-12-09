import threading

def spam(x, y):
    result = x + y
    return result

class MyThread(threading.Thread):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
    def run(self):
        spam(self.x, self.y)

t = MyThread(1,2)
t.start()
result = t.join()
print("Result:", result)  # -> None

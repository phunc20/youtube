import threading

def spam(x, y):
    result = x + y
    return result


t = threading.Thread(target=spam, args=(1,2))
t.start()
result = t.join()
print("Result:", result)  # -> None

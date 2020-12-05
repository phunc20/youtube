import thredo

def func(x, y):
    return x + y

def main():
    t = thredo.spawn(func, 2, 3)
    print("Result:", t.join())

thredo.run(main)

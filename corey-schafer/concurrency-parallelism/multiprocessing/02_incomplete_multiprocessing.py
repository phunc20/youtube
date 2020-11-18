import multiprocessing
import time

start = time.perf_counter()

def schlafen(n_sec=1):
    print(f"Sleep for {n_sec}(s) ...")
    time.sleep(n_sec)
    print(f"Done sleeping {n_sec}(s) ...")

p1 = multiprocessing.Process(target=schlafen)
p2 = multiprocessing.Process(target=schlafen)

finish = time.perf_counter()
print(f"Master finished in {round(finish-start, 2)}(s)")

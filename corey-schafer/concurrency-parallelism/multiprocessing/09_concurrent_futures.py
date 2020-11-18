import concurrent.futures
import time

start = time.perf_counter()

def schlafen(n_sec=1):
    print(f"Sleep for {n_sec}(s) ...")
    time.sleep(n_sec)
    res = f"Done sleeping {n_sec}(s) ..."
    print(res)
    return res

with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(schlafen, 2.71828)
    f2 = executor.submit(schlafen, 2.71828)
    print("f1.result() = {}".format(f1.result()))
    print("f2.result() = {}".format(f2.result()))

finish = time.perf_counter()
print(f"Master finished in {round(finish-start, 2)}(s)")

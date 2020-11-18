import multiprocessing
import time

start = time.perf_counter()

def schlafen(n_sec=1):
    print(f"Sleep for {n_sec}(s) ...")
    time.sleep(n_sec)
    print(f"Done sleeping {n_sec}(s) ...")

processes = []
n_processes = 7
for _ in range(n_processes):
    p = multiprocessing.Process(target=schlafen, args=[1.5])
    p.start()
    processes.append(p)

for p in processes:
    p.join()

finish = time.perf_counter()
print(f"Master finished in {round(finish-start, 2)}(s)")

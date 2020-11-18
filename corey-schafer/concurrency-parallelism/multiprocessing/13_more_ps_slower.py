import concurrent.futures
import time

start = time.perf_counter()

def schlafen(n_sec=1):
    print(f"Sleep for {n_sec}(s) ...")
    time.sleep(n_sec)
    res = f"Done sleeping {n_sec}(s) ..."
    #print(res)
    return res

with concurrent.futures.ProcessPoolExecutor() as executor:
    #periods = [5,4,3,2,1]
    #periods = reverse(range(1,20))
    periods = range(20,1,-1)
    Futurs = [executor.submit(schlafen, p) for p in periods]
    for F in concurrent.futures.as_completed(Futurs):
        print(F.result())

finish = time.perf_counter()
print(f"Master finished in {round(finish-start, 2)}(s)")

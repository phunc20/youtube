import concurrent.futures
import time

start = time.perf_counter()

def schlafen(n_sec=1):
    print(f"Sleep for {n_sec}(s) ...")
    time.sleep(n_sec)
    res = f"Done sleeping {n_sec}(s) ..."
    return res

with concurrent.futures.ProcessPoolExecutor() as executor:
    periods = [5,4,3,2,1]
    #Futurs = [executor.submit(schlafen, p) for p in periods]
    results = executor.map(schlafen, periods)
    #for F in concurrent.futures.as_completed(Futurs):
    for r in results:
        print(r)

finish = time.perf_counter()
print(f"Master finished in {round(finish-start, 2)}(s)")
print("You should compare this script (i.e. 14_map.py) to 12_as_completed.py")

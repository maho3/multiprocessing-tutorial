
"""
Example 2:
    How do I manage memory during multiprocessing?
"""

# Imports
import numpy as np
import multiprocessing as mp
import tracemalloc
from time import sleep

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def forked_processes():
    ### What's happening to the memory (forking)?
    tracemalloc.start()
    
    a = np.arange(1e8)

    def f(x):
        # Do some calculations
        
        print(np.sum(x))

        sleep(5.)
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"Before memory usage {current/1e6}MB")
    
    n_proc = 5
    processes = [mp.Process(target=f, args=(a,) )
                 for i in range(n_proc)]
    
    for p in processes:
        p.start()
        
    for p in processes:
        p.join()
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"After memory usage {current/1e6}MB; Peak: {peak/1e6}MB")
    tracemalloc.stop()

    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def f_spawned(x):
    # Do some calculations

    print(np.sum(x))

    sleep(5.)
    
def spawned_processes():
    ### Spawning processes does not use COW
    mp.set_start_method('spawn')
    tracemalloc.start()
    
    a = np.arange(1e8)
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"Before memory usage {current/1e6}MB")
    
    n_proc = 5
    processes = [mp.Process(target=f_spawned, args=(a,) )
                 for i in range(n_proc)]
    
    for p in processes:
        p.start()
        
    for p in processes:
        p.join()
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"After memory usage {current/1e6}MB; Peak: {peak/1e6}MB")
    tracemalloc.stop()   


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def f_bad(i):
    # Do some calculations
    sleep(2)

    return np.sum(i)

def bad_pools():
    ### mp.Pool pickles model inputs, exploding memory usage
    mp.set_start_method('fork')
    
    tracemalloc.start()
    a = np.arange(1e7)

    current, peak = tracemalloc.get_traced_memory()
    print(f"Before memory usage {current/1e6}MB")
    
    n_proc = 5
    with mp.Pool(n_proc) as pool:
        out = pool.map(f_bad, [a]*10)
    print(out)
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"After memory usage {current/1e6}MB; Peak: {peak/1e6}MB")
    tracemalloc.stop()

    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
arr = None

def f_good(i):
    global arr
    
    # Do some calculations
    sleep(2)

    return np.sum(arr)

def good_pools():
    ### We can get around this
    mp.set_start_method('fork')
    
    tracemalloc.start()
    
    global arr
    arr = np.arange(1e7)

    current, peak = tracemalloc.get_traced_memory()
    print(f"Before memory usage {current/1e6}MB")
    
    n_proc = 5
    with mp.Pool(n_proc) as pool:
        out = pool.map(f_good, [None]*10)
    print(out)
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"After memory usage {current/1e6}MB; Peak: {peak/1e6}MB")
    tracemalloc.stop()
    
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def f_shared(x, i):
    # Do some calculations
    print('Changing', i)
    x[i] = -1

def shared_memory():
    ### Use of mp's shared memory objects
    mp.set_start_method('fork')
    
    tracemalloc.start()
    
    manager = mp.Manager()
    l = manager.list(range(100))
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"Before memory usage {current/1e6}MB")
    

    n_proc = 5
    processes = [mp.Process(target=f_shared, args=(l, i) )
                 for i in range(n_proc)]
    
    for p in processes:
        p.start()
        
    for p in processes:
        p.join()
        
    print(l[:10])
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"After memory usage {current/1e6}MB; Peak: {peak/1e6}MB")
    tracemalloc.stop()

    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    forked_processes()
    spawned_processes()
    bad_pools()
    good_pools()
    shared_memory()

    
    

    
    
    

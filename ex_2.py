
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
        sleep(5.)
        print(np.sum(x))
    
    
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
    pass
    
def spawned_processes():
    ### Spawning processes does not use COW 
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def f_bad(i):
    # Do some calculations
    pass

def bad_pools():
    ### mp.Pool pickles model inputs, exploding memory usage
    pass

    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
arr = None

def f_good(i):
    pass

def good_pools():
    ### We can get around this
    pass
    
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def f_shared(x, i):
    # Do some calculations
    pass

def shared_memory():
    ### Use of mp's shared memory objects
    pass

    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    forked_processes()
#     spawned_processes()
#     bad_pools()
#     good_pools()
#     shared_memory()

    
    

    
    
    

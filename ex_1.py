
"""
Example 1:
    I have a simple for-loop that I want to speed up
"""

# Imports
import numpy as np
import multiprocessing as mp
from time import sleep

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def simple_for_loop():
    ### A simple for-loop
    a = range(5)
    out = []

    for i in a:
        # Do some calculations
        sleep(0.5)
        y = i**2

        # Print or save result
        print(y)
        out.append(y)

    print(out)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fancy_for_loop():
    ### A *fancier* for-loop
    a = range(5)

    def f(i):
        # Do some calculations
        sleep(0.5)
        y = i**2

        # Print or save result
        print(y)

        return y

    out = [f(i) for i in a]
    print(out)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def basic_Pool_map():
    ### A basic Pool map
    a = range(5)

    def f(i):
        # Do some calculations
        sleep(0.5)
        y = i**2

        # Print or save result
        print(y)

        return y

    n_proc = 5
    with mp.Pool(n_proc) as pool:
        out = pool.map(f, a)

    print(out)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def basic_Pool_imap():
    ### A Pool imap (no waiting)
    a = range(5)

    def f(i):
        # Do some calculations
        sleep(0.5)
        y = i**2

        return y

    with mp.Pool(n_proc) as pool:
        for i in pool.imap(f, a):
            print(i)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Pool_map_with_progress():
    ### Pool map with *progress bar*
    import tqdm
    a = range(100)

    def f(i):
        # Do some calculations
        sleep(0.5)
        y = i**2

        return y

    n_proc = 5
    with mp.Pool(n_proc) as pool:
        out = list(tqdm.tqdm(pool.imap(f, a), total=len(a)))

    print(out)
    
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
def basic_mp_Process():
    ### Barebones Process handling (no returns)
    a = range(5)

    def f(i):
        # Do some calculations
        sleep(0.5)
        y = i**2

        # Print result
        print(y)

    n_proc = 5
    processes = [mp.Process(target=f, args=(a[i],) )
                 for i in range(n_proc)]
    
    for p in processes:
        p.start()
        
    for p in processes:
        p.join()
        
        
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    simple_for_loop()
    basic_Pool_map()
    basic_Pool_imap()
    Pool_map_with_progress()
    basic_mp_Process()
    
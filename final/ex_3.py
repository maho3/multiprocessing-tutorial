
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
def f1(q):
    q.put('Hello I am subprocess 1')
    sleep(0.05)
    print(q.get())
    q.put('Hello father!')

def f2(q):
    print(q.get())
    q.put('Nice to meet you, I am subprocess 2.')

def queue_example():
    ### Demonstrate Queue messaging
    q = mp.Queue()
    
    p1 = mp.Process(target=f1, args=(q,))
    p2 = mp.Process(target=f2, args=(q,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(q.get())

    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
def f3(conn):
    conn.send('Psst, I have a secret.')
    print(conn.recv())
    conn.close()

def f4(conn):
    print(conn.recv())
    conn.send('What is it?')
    
def pipe_example():
    ### Demonstrate Pipe messaging
    
    end1, end2 = mp.Pipe()
    
    p1 = mp.Process(target=f3, args=(end1,))
    p2 = mp.Process(target=f4, args=(end2,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()
        
def lock_example():
    ### Demonstrate printing Locks
    lock = mp.Lock()

    for num in range(10):
        mp.Process(target=f, args=(lock, num)).start()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
if __name__ == '__main__':
#     queue_example()
#     pipe_example()
    lock_example()
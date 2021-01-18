
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
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def basic_Pool_map():
    ### A basic Pool map
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def basic_Pool_imap():
    ### A Pool imap (no waiting)
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Pool_map_with_progress():
    ### Pool map with *progress bar*
    pass
    
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
def basic_mp_Process():
    ### Barebones Process handling (no returns)
    pass
        
        
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    simple_for_loop()
#     basic_Pool_map()
#     basic_Pool_imap()
#     Pool_map_with_progress()
#     basic_mp_Process()
    
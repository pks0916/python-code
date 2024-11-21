"""Simple script to run all 3 contains algorithms. Quick way to test running times."""

import time, random
from lab6 import OrderedList as OL
random.seed(652)    # Fix the random seed.  If there is a bug, it happens
                    # the same way every time.

def time_f(func, args, trials=5):
    """Returns minimum time trial of func(args)"""
    t_min = float('inf')

    for i in range(trials):
        start = time.time()
        func(args)
        end = time.time()
        if end-start < t_min: t_min = end - start

    return t_min

n = int(100E6) # You may need to modify (bigger or smaller) depending on the speed of your hardware
ol1 = OL([i for i in range(n)])
print(f"n = {n}")

# We commit a cardinal sin below in the interest of education - you should 
# *never* call a private attribute outside of it's class.

print(f"{time_f(ol1._contains_list, -1)*1E3:.2f} ms - t_contains_list")
print(f"{time_f(ol1._contains_bs_slow, -1)*1E3:.2f} ms - t_contains_bs_slow")
print(f"{time_f(ol1.__contains__, -1)*1E3:.2f} ms - t_contains")


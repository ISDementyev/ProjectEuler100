import numpy as np
from numba import jit

# non-optimized - roughly 67.5 microseconds
def sum_multiples_3_5(N):    
    return sum([i for i in range(N) if i % 3 == 0 or i % 5 == 0])

# optimized with numpy and numba (just-in-time compilation) - roughly 20 times faster at 3.25 microseconds
@jit
def sum_mults_np(N):
    nums = np.arange(N)
    return np.sum(np.where((nums % 3 == 0) | (nums % 5 == 0), nums, 0))

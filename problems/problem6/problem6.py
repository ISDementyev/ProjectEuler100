from numba import jit, int64
import numpy as np

# Unoptimized version
def diff(N):
    return np.sum(np.arange(1, N + 1)) ** 2 - np.sum(np.arange(1, N + 1) ** 2)
  
# Optimized version - roughly 20 times faster
@jit(int64(int64))
def diff_j(N): 
    return np.sum(np.arange(1, N + 1)) ** 2 - np.sum(np.arange(1, N + 1) ** 2)

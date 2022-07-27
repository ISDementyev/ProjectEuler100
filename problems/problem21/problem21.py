from numba import jit

################## helper functions ########################################################
def d(n):
    return sum([i for i in range(1, n) if n % i == 0])

@jit
def dj(n):
    return sum([i for i in range(1, n) if n % i == 0])

################## main functions ##########################################################
def problem21(N):
    amicables = set()
    
    for i in range(1, N):
        d_val = d(i)
        
        if i == d(d_val) and i != d_val:
            amicables.add(i)
            amicables.add(d_val)
            
    return sum(amicables)

def problem21_faster(N): # overall speedup is roughly 30-fold (excluding loading numpy and jit)
    amicables = set()
    
    for i in range(1, N):
        d_val = dj(i)
        
        if i == dj(d_val) and i != d_val:
            amicables.add(i)
            amicables.add(d_val)
            
    return sum(amicables)

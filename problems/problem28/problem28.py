from numba import jit

# unoptimized
def Problem28(n):
    n = (n - 1) // 2
    
    # generate diagonal values:
    start = 3
    Sum = 3
    
    for i in range(1, n + 1):
        if i == 1:
            times = 2
        else:
            times = 3
            
        for _ in range(times + 1):
            start += i * 2
            Sum += start
                
    return Sum + 1

@jit
def Problem28J(n):
    n = (n - 1) // 2
    
    # generate diagonal values:
    start = 3
    Sum = 3
    
    for i in range(1, n + 1):
        if i == 1:
            times = 2
        else:
            times = 3
            
        for _ in range(times + 1):
            start += i * 2
            Sum += start
                
    return Sum + 1
  
print(Problem28(1001))
print(Problem28J(1001)) # roughly 160-223x faster

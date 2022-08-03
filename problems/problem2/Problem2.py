from math import sqrt

# helpers
def FibonacciBinet(N):
    phi = (1 + sqrt(5)) / 2
    phiN = (1 - sqrt(5)) / 2
    
    return round((phi ** N - phiN ** N) / sqrt(5))

# main - currently unoptimized
def Problem2():
    i = 2

    while (FibonacciBinet(i) < 4_000_000):
        i += 1

    return sum([j for j in Fibonacci(i - 1) if j % 2 == 0])

# More simpler and easier to read, but not much faster
def Problem2Simpler():
    i = 2
    Sum = 0
    
    while (FibonacciBinet(i) < 4_000_000):
        Term = FibonacciBinet(i)
        
        if Term % 2 == 0:
            Sum += Term
            
        i += 1
    
    return Sum
  
Problem2Simpler()

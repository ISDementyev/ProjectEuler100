from math import sqrt

# helpers
def FibonacciBinet(N):
    phi = (1 + sqrt(5)) / 2
    phiN = (1 - sqrt(5)) / 2
    
    return round((phi ** N - phiN ** N) / sqrt(5))

# main - currently unoptimized
def Problem9():
    i = 2

    while (FibonacciBinet(i) < 4_000_000):
        i += 1

    return sum([j for j in Fibonacci(i - 1) if j % 2 == 0])
  
Problem9()

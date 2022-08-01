from numba import jit

# helpers
def Factorial(n):
    if n == 0 or n == 1:
        return 1
    
    Fac = 1
    
    for i in range(1, n + 1):
        Fac *= i
        
    return Fac

@jit
def FactorialJ(n):
    if n == 0 or n == 1:
        return 1
    
    Fac = 1
    
    for i in range(1, n + 1):
        Fac *= i
        
    return Fac
  
# main
# unoptimized
def Problem34(n):
    ProblemList = []
    
    for i in range(10, n + 1):
        iList = [int(j) for j in list(str(i))]
        
        FactorialSum = sum([Factorial(k) for k in iList])
        
        if FactorialSum == i:
            ProblemList.append(i)
            
    return sum(ProblemList)
  
# main
# slightly faster (~500 ms less)
def Problem34Simpler(n):
    Total = 0
    
    for i in range(10, n + 1):
        FacSum = 0
        
        for Digit in str(i):
            FacSum += Factorial(int(Digit))
        
        if FacSum == i:
            Total += i
            
    return Total

# main
# more optimized
# 2.3x faster than original
def Problem34J(n):
    Total = 0
    
    for i in range(10, n + 1):
        FacSum = 0
        
        for Digit in str(i):
            FacSum += FactorialJ(int(Digit))
        
        if FacSum == i:
            Total += i
            
    return Total

Problem34J(1000000)

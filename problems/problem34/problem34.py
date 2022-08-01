# helpers
def Factorial(n):
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
  
  Problem34(int(1e6))

# Unoptimized
def Fibonacci(n): # helper function to return the ith fibonacci number
    if n == 1 or n == 2:
        return 1
    
    values = [1, 1]
    
    for i in range(2, n):
        fib = values[i - 1] + values[i - 2]
        values.append(fib)
        
    return values[-1]


def Problem25(): # main
    i = 1
    val = Fibonacci(i)
    
    while len(str(val)) < 1000:
        i += 1
        val = Fibonacci(i)
        
    return i
  
  Problem25()

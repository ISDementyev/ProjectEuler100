# unoptimized
def Problem28(n):
    n = (n - 1) // 2
    
    # generate diagonal values:
    diagonals = [3]
    start = 3
    
    for i in range(1, n + 1):
        if i == 1:
            times = 2
        else:
            times = 3
            
        for _ in range(times + 1):
            start += i * 2
            diagonals.append(start)
                
    return sum(diagonals) + 1 # returns sum(diagonals) + 1 since diagonal generation does not include 1x1 case
  
print(Problem28(1001))

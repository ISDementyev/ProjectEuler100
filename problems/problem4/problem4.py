from numba import jit

def is_palindrome(n):
    n = str(n)
    return n[::-1] == n

@jit
def is_palindromeJ(n):
    n = str(n)
    
    return n[::-1] == n

@jit
def problem_4_jit(): # roughly twice as fast
    palindromes = [i * j for i in range(1, 1000) for j in range(i, 1000) if is_palindromeJ(i * j)]
    
    return max(palindromes)
    
def problem_4():
    return max([i * j for i in range(1, 1000) for j in range(i, 1000) if is_palindrome(i * j)])

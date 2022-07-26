def is_palindrome(n):
    n = str(n)
    
    if n[::-1] == n:
        return True
    else:
        return False

def problem_4():
    palindromes = [i * j for i in range(1, 1000) for j in range(1, 1000) if is_palindrome(i * j)]
    
    return max(palindromes)

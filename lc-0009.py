'''
Given an integer x, return true if x is a palindrome, and false otherwise.'''

def isPalindrome(x: int) -> bool:
    x = str(x)
    l,r = 0, len(x)-1
    while l <= r:
        if (x[l] != x[r]):
            return False
        else:
            l += 1
            r -= 1
    return True

s = 123321
print(isPalindrome(s))
s = 521
print(isPalindrome(s))

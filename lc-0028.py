'''
Given two strings needle and haystack, return the index of the first occurrence of
needle in haystack, or -1 if needle is not part of haystack.
'''

def strStr(haystack: str, needle: str) -> int:
    a = len(haystack)
    b = len(needle)
    c = a-b
    if c<0:
        return -1
    elif c==0:
        if haystack == needle:
            return 0
        else:
            return -1
    else:
        for i in range(c+1):
            if haystack[i:i+b] == needle:
                return i
            else:
                continue
        return -1


haystack = 'sadbutsad'
needle = 'sad'
print(strStr(haystack,needle))
haystack = 'sadbutsad'
needle = 'but'
print(strStr(haystack,needle))
haystack = 'xyz'
needle = 'z'
print(strStr(haystack,needle))
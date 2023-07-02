'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range
[-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

def reverse(x: int) -> int:
    def rev(d):
        a, r = 0, 0
        while d !=0:
            r = d%10
            d = d//10
            a = (a+r)*10
        if int(a/10) > 2**31:
            return 0
        else:
            return int(a/10)

    if x >= 0:
        m = rev(x)
        return m
    else:
        m = rev(-x)
        return -m


d= 98
print(reverse(d))
d = -122
print(reverse(d))
d = -239
print(reverse(d))

print(2**31)

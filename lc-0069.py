'''Given a non-negative integer x, return the square root of x rounded down to the
nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
eg: Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the
nearest integer, 2 is returned.'''

def mySqrt(x: int) -> int:
    low = 0
    high = x
    current = (high + low)/2
    esp = 0.01
    if x ==1:
        return 1
    while esp >= 0.001:
        current = (high + low)/2
        error = x - current*current
        if error > 0:
            low = current
        else:
            high = current
        esp = abs(error)
        continue
    sqrt = int(current)
    return sqrt

x = 8
print(mySqrt(x))
x = 16
print(mySqrt(x))
x = 10
print(mySqrt(x))
x = 2147395600
print(mySqrt(x))

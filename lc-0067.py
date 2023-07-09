'''Given two binary strings a and b, return their sum as a binary string.'''

def addBinary(a: str, b: str) -> str:
    d = ""
    c = 0 # carry
    i = len(a)-1
    j = len(b)-1

    while i >= 0 or j >= 0:
        dig_a = int(a[i] if i >= 0 else 0)
        dig_b = int(b[j] if j >= 0 else 0)

        r = (dig_a + dig_b + c)%2
        c = (dig_a + dig_b + c)//2
        d = str(r) + d
        i -=1
        j -=1

    if c:
        d = '1' + d

    return d

'''
Python excepts (a[i] if i>= 0 else 0) as valid and shows list out 
of range in (a[i] if a[i] else 0)
'''
a = '11'
b='11'
print(addBinary(a,b))
a = '11'
b='1'
print(addBinary(a,b))
a = '11'
b='10101'
print(addBinary(a,b))
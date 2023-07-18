'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.
eg:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
'''

def generate(numRows: int) -> list[list[int]]:
    d = []
    for i in range(numRows):
        l = []
        if i == 0:
            l.append(1)
        else:
            d[i - 1].append(0)
            d[i - 1].insert(0, 0)
            x = 0
            for j in range(len(d[i - 1]) - 1):
                x = d[i - 1][j] + d[i - 1][j + 1]
                l.append(x)
            d[i - 1].pop()
            d[i - 1].pop(0)
        d.append(l)
    return d

print(generate(7))
print('-*'*5)
print(generate(9))
print('-*'*5)
print(generate(1))
print('-*'*5)
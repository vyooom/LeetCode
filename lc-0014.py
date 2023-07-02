'''Write a function to find the longest common prefix string amongst an array
of strings. If there is no common prefix, return an empty string.'''

def longestCommonPrefix(strs) -> str:
    def compare(a,b):
        d = ""
        for i in range(min(len(a), len(b))):
            if a[i] == b[i]:
                d += a[i]
            else:
                return d
        return d
    i = 0
    d = strs[0]
    if len(strs) == 1:
        return d
    else:
        while i < len(strs)-1:
            d = compare(d, strs[i+1])
            if d == "":
                return d
            else:
                i +=1
        return d


strs = ['flower', 'flow', 'flown']
print(longestCommonPrefix(strs))
strs2 = ['flwer', 'flow', 'flown']
print(longestCommonPrefix(strs2))
strs = ['flyer']
print(longestCommonPrefix(strs))
strs = ['cir', 'car']
print(longestCommonPrefix(strs))
strs = ['cir', 'dog']
print(longestCommonPrefix(strs))
'''
Given a string s, find the length of the longest substring
without repeating characters.
Eg:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Notice that the
answer must be a substring, "pwke" is a subsequence and not a substring.
'''

def lengthOfLongestSubstring(s: str) -> int:
    d = {}
    large = 0
    current = 0
    start = 0
    for count, charc in enumerate(s):
        if charc in d and d[charc] >= start:
            current = count - d[charc]
            start = d[charc]+1
        else:
            current += 1
        d[charc] = count
        large = (current if current>large else large)
    return large

s = 'pwwkew'
print(lengthOfLongestSubstring(s))

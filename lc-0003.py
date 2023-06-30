'''
Given a string s, find the length of the longest substring
without repeating characters.
Eg:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring,
"pwke" is a subsequence and not a substring.
'''

def lengthOfLongestSubstring(s: str) -> int:
    d = {}
    large = 0
    current = 0
    start = 0
    for count, charc in enumerate(s):
        if charc in d and current < count+1:
            large = (start if start > large else large)
            current = 1
            start = 0
            pass
        else:
            d[charc] = count
            current += 1

        start += 1
        large = (current if current>large else large)


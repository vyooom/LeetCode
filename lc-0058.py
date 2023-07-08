'''Given a string s consisting of words and spaces, return the length of the last
word in the string. A word is a maximal substring consisting of non-space characters only.'''

def lengthOfLastWord(s: str) -> int:
    w = s.strip()
    if len(w) == 0:
        return 0
    i = -1
    c = 0
    for j in range(len(w)):
      if w[i] != " ":
          c +=1
          i -=1
      else:
          break
    return c

s = "Hello World"
print(lengthOfLastWord(s))
s = "Hello World    "
print(lengthOfLastWord(s))
s = ""
print(lengthOfLastWord(s))
s = " "
print(lengthOfLastWord(s))
s = "a"
print(lengthOfLastWord(s))
'''
Given a string s, return true if it is a palindrome, or false otherwise.
'''
# the below code fails on recursion of > 1000 loops
# hence a different program is to be made
'''
def isPalindrome(s: str) -> bool:
    if len(s) == 0 or len(s) == 1:
        return True
    else:
        s = s.lower()
        for character in s:
            if character not in "abcdefghijklmnopqrstuvwxyz0123456789":
                s = s.replace(character, "")

        def palCh(string):
            if not string or len(string) == 1:
                return True
            else:
                if string[0] != string[-1]:
                    return False
                else:
                    return palCh(string[1:-1])

        return palCh(s)
'''
def isPalindrome(s: str) -> bool:
    def cleanString(inString):
        inString = inString.lower()
        for character in inString:
            if character not in "abcdefghijklmnopqrstuvwxyz0123456789":
                inString = inString.replace(character, "")
        return inString

    if len(s) == 0 or len(s) == 1:
        return True
    else:
        s = cleanString(s)

    while bool(s) == True:
        if s[0] == s[-1]:
            s = s[1:-1]
        else:
            return False
    return True


k = "Ma la ya la m"
print(isPalindrome(k))
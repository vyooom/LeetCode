'''Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.'''

def isValid(s: str) -> bool:
    '''
    The code uses a stack to track the opening parentheses.
    The stack is a data structure that stores elements in a last-in, first-out (LIFO) order.
    This means that the last element that was pushed onto the stack is the first element
    that will be popped off the stack.

    When an opening parenthesis is encountered, it is pushed onto the stack.
    When a closing parenthesis is encountered, it is popped off the stack.
    If the closing parenthesis does not match the top of the stack, then the string is invalid.
    :param s:
    :return:
    '''
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack

s = '(){}[]'
print(isValid(s))
s = '({[]}){}[]'
print(isValid(s))
s = '(){}[]]'
print(isValid(s))

'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''


def addTwoNumbers(l1, l2):
    l = []
    i = 0
    c = 0
    a = 0
    b = 0
    while i < max(len(l1), len(l2)):
        a = (l1[i] if l1[i] else 0)
        b = (l2[i] if l2[i] else 0)
        t = a + b + c
        d = (t if t<10 else t-10)
        l.append(d)
        c = (0 if t < 10 else 1)
        i +=1

    if c==1:
        l.append(1)
    return l



l1 = [2,4,9]
l2 = [5,6,4]
x = addTwoNumbers(l1,l2)
print(x)

# solution [7, 0, 4, 1]
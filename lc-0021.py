'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together
the nodes of the first two lists. Return the head of the merged linked list.

'''

def merge(l,r):
    result = []
    i, j = 0,0

    while i< len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    result += l[i:]
    result += r[j:]

    return result

'''
The solution is not accepted because of linked list. and len method not available in linked list.
'''
a = [5,9,15,86,98]
b = [2,7,21,36,91,100]
print(merge(a,b))

a = []
b = []
print(merge(a,b))
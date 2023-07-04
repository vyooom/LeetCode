'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order of the
elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to
do the following things:

Change the array nums such that the first k elements of nums contain the unique
elements in the order they were present in nums initially. The remaining elements
of nums are not important as well as the size of nums.

Return k.
'''


def removeDuplicates(nums: list[int]) -> int:
    res = []
    k = 0
    i = 0
    while i < len(nums):
        if nums[i] not in res:
            res.append(nums[i])
        i += 1
    i = 0
    while i < len(res):
        nums[i] = res[i]
        i += 1
''' Leetcode doesnot accept the assignment nums = res, hence the second while loop is made.'''
    k = len(res)
    return k

a =[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(a))


def removeDuplicates2(nums: list[int]) -> int:
    i = 0
    res = set()
    while i < len(nums):
        if nums[i] in res:
            nums.remove(nums[i])
        else:
            res.add(nums[i])
            i += 1

    k = len(nums)
    return k

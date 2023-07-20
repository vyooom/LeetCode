'''
Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.
'''

def containsDuplicate(nums: list[int]) -> bool:
    if not nums or len(nums) == 1:
        return False
    d = {}
    for key, num in enumerate(nums):
        if num in d:
            return True
        else:
            d[num] = key
    return False

nums = [3]
print(containsDuplicate(nums))
nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))
nums = [7,6,71,8]
print(containsDuplicate(nums))
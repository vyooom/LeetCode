'''
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

def twoSums(nums, target):
    i = 0
    while i < len(nums):
        j = i+1
        while j < len(nums):
            if nums[i]+nums[j] == target:
                return i,j
            j += 1
        i += 1

'''
Solution submitted on 27/06/2023
Runtime 7269 ms beats 7.4%
Memory 17 MB beats 99.74%
'''
nums = [3,2,4]
target = 6
x = twoSums(nums, target)
print(x)






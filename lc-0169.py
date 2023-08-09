'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''


def majorityElement(nums: list[int]) -> int:
    nums.sort()
    count = 0
    majCount = 0
    majEle = nums[0]
    curEle = nums[0]
    for num in nums:
        if curEle == num:
            count += 1
            if count > majCount:
                majCount = count
                majEle = curEle
        else:
            count = 1
            curEle = num

    return majEle

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
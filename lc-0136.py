'''
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant
extra space.
'''

def singleNumber(nums: list[int]) -> int:
    nums.sort()
    k = nums[0]
    for i in range(len(nums)):
        if i < len(nums) - 1:
            if nums[i] not in nums[i + 1:] and nums[i] not in nums[0:i]:
                k = nums[i]
                break
            else:
                continue
        else:
            if nums[i - 1] != nums[i]:
                k = nums[i]

    return k

nums = [4,1,2,1,2]
print(singleNumber(nums))


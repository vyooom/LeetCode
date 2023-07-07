def removeElement(nums: list[int], val: int) -> int:
    i = 0
    ind = []
    while i < len(nums):
        if nums[i] == val:
            ind.append(i)
            # just remove the element and no need to increase i as len decreased
            nums.remove(nums[i])
        else:
            i += 1
    k = len(nums)
    a = len(nums)-1
    j=0
    if nums == []:
        # for empty list
        return k
    else:
        for l in ind:
            t =nums[a]
            # as the stored indexes are one sort evertime after removal as/
            # original length kept on decreasing
            nums.insert(l+j, t)
            j += 1

    return nums, k, ind


nums = [3,2,2,3, 2, 2, 5,6,7]
print(nums)
print(removeElement(nums, 2))
print('+*'*8)
nums = [0,1,2,2,3,0,4,2]
print(nums)
print(removeElement(nums, 2))
print('-*'*8)
nums= [3,3]
print(nums)
print(removeElement(nums, 3))
print('-*'*8)
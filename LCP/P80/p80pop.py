def removeDuplicates(nums) -> int:
    for i in reversed(range(len(nums))):
        #print("nums[i], nums[i-1], nums[i-2]", nums[i], nums[i-1], nums[i-2])
        if i<2:
            break
        if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
            nums.pop(i)
    #print(nums)
    return (len(nums))
nums = [1,1,1,2,2,3]
nums1 = [2,2,2,2,2,2,5,6,8,4,6,8,4,5,6]
nums2 = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums2))

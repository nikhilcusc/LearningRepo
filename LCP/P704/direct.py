def bins(nums,target):
    high = len(nums)-1
    low=0
    if target not in nums:
        return -1
    while high>low:
        mid = int((high+low)/2)
        print("high",high,"\t low", low, "\t mid",mid)
        
        if nums[mid]==target:
            return(mid)
        if nums[mid]<target:
            low = mid
        else:
            high = mid
    return(-1)
nums ,target =  [-1,0,3,5,9,12], 9
nums2, target2 = [-1,0,3,5,9,12], 2

def bins2(nums,target):
    return -1 if target not in nums else nums.index(target)
print(bins2(nums,target2))


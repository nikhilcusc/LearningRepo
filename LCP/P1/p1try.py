
list1 = [3,5,2,6,2]
slist1 = []
slist1 = list1
slist1.sort()
print (list1,slist1)
print(list1.index(3))


def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #nums.sort()
        for num in nums:
            k=0
            while k < len(nums):
                #f"k {k} at {nums.index(k)} ,num at {nums.index(num)} and  {target}"
                print(nums[k],k,num,nums.index(num),target)
                if nums.index(num)== k:
                    k+=1
                    continue    
                
                if nums[k]>target or num > target:
                    k+=1
                    continue
                if nums[k]+num==target :
                    return [nums.index(num), k]
                k+=1
        return "not Possible"

def sum2(nums, target):
    for num in nums:
            k=target - num
            kn=nums.index(num)
            nums[kn]=0
            if k in nums and nums.index(k)!=kn:
                return [kn,nums.index(k)]
                
    return "not Possible"


nums = [2, 7, 11, 15]
nums2 = [3,2,4]
nums3=[3,3]
target = 6
print("Function ")
print(sum2(nums2,target))
#print(3 in nums2)
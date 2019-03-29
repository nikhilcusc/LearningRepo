def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #nums.sort()
        for num in nums:
            k=target - num
            kn=nums.index(num)
            nums[kn]=-1000
            if k in nums and nums.index(k)!=kn:
                return [kn,nums.index(k)]
                
        return "not Possible"
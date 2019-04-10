
def PredictTheWinner(nums):
    
    if len(nums)==1:
        return True

    def winner(nums, s, e):
        global memo
        if s==e:
            return nums[s]
        if memo[s][e] !=None:
            return memo[s][e]
        a = nums[s] - winner(nums, s+1, e)
        b = nums[e] - winner(nums, s, e-1)

        memo[s][e] = max(a,b)
        print("at ",s , "and ", e, " memo is : ", memo)
        return memo[s][e]
    
    return winner(nums, 0, len(nums)-1)>=0


        
nums = [1, 5, 2]
nums1 = [1, 5, 233, 7]
nums=nums1
memo = [[None for i in range(len(nums))] for j in range(len(nums))]
print(memo)
print(PredictTheWinner(nums))
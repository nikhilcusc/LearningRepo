def PredictTheWinner(nums):
    if len(nums)==1:
        return True
    def winner(nums, s, e, turn):
        if s==e:
            return turn*nums[s]
        a = turn * nums[s] + winner(nums, s+1, e, -turn)
        b = turn * nums[e] + winner(nums, s, e-1, -turn)
        return turn * max(turn*a, turn * b)
    
    return winner(nums, 0, len(nums)-1, 1)>=0


        
nums = [1, 5, 2]
nums1 = [1, 5, 233, 7]
print(PredictTheWinner(nums))
#greedy approach - not optimal
def PredictTheWinner(nums):
    score1 = 0
    score2 = 0
    print(nums)
    while len(nums)>1:
        score1t = max(nums[0],nums[-1])
        print("player1's turn takes", score1t)
        if nums[0]> nums[-1]:
            nums = nums[1:]
        else:
            
            nums = nums[:-1]
        #print(nums)
        score1 +=score1t

        score2t = max(nums[0],nums[-1])
        print("player2's  turn takes",score2t)
        if nums[0]> nums[-1]:
            nums = nums[1:]
        else:
            
            nums = nums[:-1]
        print(nums)
        score2 +=score2t
    if len(nums)==1:
        score1+=nums[0]

        
    print(score1, score2)
    return score2<score1
        

        
nums = [1, 5, 2]
nums1 = [1, 5, 233, 7]
print(PredictTheWinner(nums))
def sortcolours(nums):
    colunique = set(nums)
    count=[0]*len(colunique)
    
    #count = [0,0,0]
    print(count)
    for i in nums:
        count[i]+=1
    print(count)
    index=0
    for i in colunique:
        for j in range(count[i]):
            nums[index] = i
            index+=1
    return nums

ll = [2,0,2,1,1,0,3,3,3,3,3,3,4,4,4]
print(sortcolours(ll))

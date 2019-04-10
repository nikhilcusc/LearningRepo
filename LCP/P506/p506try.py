def li(nums):
    nums2 = nums
    print(nums)
    nums2 = sorted(nums, reverse=True)
    print(nums, nums2)
    ranks = []
    for j  in nums:
        rank = nums2.index(j)+1
        print("ranks",rank, "j",j)
        if rank==1:
            rank = "Gold Medal"
        elif rank==2:
            rank = "Silver Medal"
        elif rank==3:
            rank = "Bronze Medal"
        else:
            rank = str(rank)
        ranks.append(rank)

    return ranks

l = [5, 4, 3, 2, 1]
lk = [10,3,8,9,4]
print(li(lk))
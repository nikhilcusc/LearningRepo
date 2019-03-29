def f1(nums,val):
    nums.append(val)
    nums.sort(reverse=True)
    print(nums)


lf1 = [4,5,8,2]

print(f1(lf1,3))
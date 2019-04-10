def singleNumber(nums):
    uniqueEle =list( set(nums))
    for i in nums:
        if i in uniqueEle:
            uniqueEle.remove(i)
        else:
            uniqueEle.add(i)
    return uniqueEle


nusm = [1,2,1,3,2,5]
#print(nusm)
print(singleNumber(nusm))
def singleNumber(nums):
    uniqueEle =list( set(nums))
    print(uniqueEle)
    dict1 = {}
    for i in nums:
        try:
            dict1[i]+=1
        except KeyError:
            dict1[i]=1
    print(dict1)
    
    j = sorted(dict1.items(),key=lambda x : x[1])
    print(j)
    a = j[0][0]
    b = j[1][0]
    return (a,b)


nusm = [1,2,1,3,2,5]
#print(nusm)
print(singleNumber(nusm))
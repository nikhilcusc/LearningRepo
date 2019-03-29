def sN(nums):
    repN=dict()
    for i  in nums:
        try:
            repN[i]+=1
        except KeyError:
            repN[i]=1
    print(repN)
    for key, value in repN.items():
        #print(key, value)
        if value == 1:
            return key

list1 = [2,2,3,2]

print(sN(list1))
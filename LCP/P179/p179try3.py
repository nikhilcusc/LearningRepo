
def largNum(nums):
    srot = {}
    for k in  range(9,1,-1):
        srot[k] = []
    
    for ele in nums:
        digit = int(ele / (pow(10,len(str(ele))-1)))
        print(ele,digit)
        srot[digit].append(str(ele))    

    str1=""
    
    for key, values in srot.items():
        print(values)
        values.sort(reverse=True)
        print(values)
        partstr = ''.join(str(e) for e in values)
        #print(partstr, partstr=="")
        if partstr!="":
            str1+=partstr
    return str1  

list1 = [3,30,34,5,9]

print(largNum(list1))
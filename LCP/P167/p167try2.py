def twoSum( numbers, target):
    if len(numbers)==1:
        return False
    index1 =0 
    index2=len(numbers)-1
    
    while index1 < index2:
        if numbers[index1] + numbers[index2] == target:
            return (index1+1,index2+1)
        if numbers[index1] + numbers[index2] > target:
            index2-=1
        else:

            index1+=1
    return False
    



numbers = [2,7,11,15]
numbers2 = [2,25,75]
target = 100

print(twoSum(numbers2, target))
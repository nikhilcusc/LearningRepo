def twoSum( numbers, target):
    if len(numbers)==1:
        return False
    index1 =0 
    index2=1
    print(len(numbers))
    while index1 <len(numbers):
        index2=0
        while index2 < len(numbers):
            print("index1", index1, "index2", index2)
            if numbers[index1] + numbers[index2] == target and index1!=index2:
                return (index1+1,index2+1)
            index2+=1
        index1+=1
    return False
    



numbers = [2,7,11,15]
numbers2 = [2,25,75]
target = 100

print(twoSum(numbers2, target))
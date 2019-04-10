def removeDuplicates(nums) -> int:
    fixed = 0
    set1 = set(nums)
    for j in set1:
        counter = 0
        print("\n\nconsidering ",j, " with counter ", counter, " with nums now  is :",nums)
        for i in range(len(nums)):
            if nums[i]==j:
                counter+=1
            print("nums[i], counter", nums[i], counter)
            if counter>2:
                #shift the array one element back
                #print("Counter value over 2", counter,nums[i])
                fixed+=1
                while i<len(nums)-1:
                    print(i)
                    nums[i] = nums[i+1]
                    i+=1
                
                nums[-1] = -float("Inf")
                print("Array after fixing ", j , " is  : ",nums)
                break

    print("\n \n \n Final nums ",nums)    
    return len(nums) - fixed

def removeDuplicates2(nums) -> int:
    fixed, j  = 0, 0
    set1 = list(set(nums))
    while j < (len(set1)):
        counter = 0
        print("\n\nconsidering ",set1[j], " with counter ", counter, " with nums now  is :",nums)
        for i in range(len(nums)):
            if nums[i]==set1[j]:
                counter+=1
            print("nums[i], counter", nums[i], counter)
            if counter>2:
                #shift the array one element back
                #print("Counter value over 2", counter,nums[i])
                fixed+=1
                while i<len(nums)-1:
                    print(i)
                    nums[i] = nums[i+1]
                    i+=1
                
                nums[-1] = -float("Inf")
                print("Array after fixing ",set1[j] , " is  : ",nums)
                j-=1 # run the check again on the same element, as this element could be repeated more than 3 times
                break
        j+=1
    print("\n \n \n Final nums ",nums)    
    return len(nums) - fixed

nums = [1,1,1,2,2,3]
nums1 = [2,2,2,2,2,2,5,6,8,4,6,8,4,5,6]
nums2 = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates2(nums1))
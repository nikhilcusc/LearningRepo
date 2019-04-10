def merge(l1,m,l2,n):
    j=0
    while j<len(l2):
        
        l1[m+j]=l2[j]
        j+=1
    print(l1)
    return sorted(l1)

nums1 = [1,2,4,5,6,0]
nums2 = [3]     
m,n = 5,1

print(merge(nums1, m, nums2, n))


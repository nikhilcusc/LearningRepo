def canThreePartsEqualSum( A) -> bool:

    sum1 = sum(A)/3
    print(sum1)
    ind1, ind2 = 0, 0
    tempsum = A[ind1] 
    while tempsum!=sum1 and ind1<len(A)-1:
        ind1+=1
        tempsum+=A[ind1]
    print(ind1)
    ind2 = ind1+1
    if ind2 < len(A):
        tempsum = A[ind2]
    else:
        return False

    while tempsum!=sum1 and ind2<len(A)-1:
        ind2+=1
        tempsum+=A[ind2]
    print(ind2,(A[ind2+1:]),sum(A[ind2:]))
    return sum(A[ind2+1:]) == sum1

        


     



k1 = [0,2,1,-6,6,-7,9,1,2,0,1]
k2 = [0,2,1,-6,6,7,9,-1,2,0,1]
k3 = [3,3,6,5,-2,2,5,1,-9,4]
print(canThreePartsEqualSum(k3))
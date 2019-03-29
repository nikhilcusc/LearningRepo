def binsearch(arr, low, high, target):
    
    mid = int((low+high)/2)
    #print(low, mid, high)
    if low<=high:
        if target == arr[mid]:
            return True
        if target> arr[mid]:
            return binsearch(arr, mid+1, high, target)
        if target < arr[mid]:
            return binsearch(arr, low, mid-1, target)
    else:
        return False
def linsearch2(arr, low, high, target):
    for ar in arr:
        if ar>target:
            return arr.index(ar)-1
    return len(arr)-1
    '''
    mid = int((low+high)/2)
    #print(low, mid, high)
    if low<=high:
        if target == arr[mid]:
            return True
        if target> arr[mid]:
            return binsearch(arr, mid+1, high, target)
        if target < arr[mid]:
            return binsearch(arr, low, mid-1, target)
    else:
        return mid
    '''

def binsearcher(arr,target):
    if len(matrix)==0:
            return False
    try:
        firstcol = list(i[0] for i in (matrix))
    except IndexError:  
        return False
    print(firstcol)
    rowind = linsearch2(firstcol, 0, len(firstcol)-1,target)
    print(rowind, arr[rowind], target)

    return binsearch(arr[rowind],0, (len(arr[rowind])-1), target)

def matsearch(matrix,target):

    return binsearcher(matrix,target)

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 34
l = [1,   3,  5,  7]
print(matsearch(matrix,target))
#print(binsearch(l,0, (len(l)-1),target))
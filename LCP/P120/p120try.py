# The question asks a path, that means, we cannot jump very far from on row to another. The element from next row should be adjacent.
def minimumTotal(triangle):
    sum1 = 0
    for row in triangle:
        print( min(row))
        sum1+= min(row)
    return sum1

l = [[2],[3,4],[6,5,7],[4,1,8,3]]
l2= [[-1],[2,3],[1,-1,-3]]
print(minimumTotal(l2))
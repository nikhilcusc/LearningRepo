def minimumTotal(triangle):
    sum1 = []
    height = len(triangle)
    for h in range(1,height+1):
        sum1.append([0]*h)

    for h in range(height):
        sum1[height-1][h] = triangle[height-1][h]

    for i in range(height-2,-1,-1):
        for j in range(i+1):
            sum1[i][j] = min(sum1[i+1][j], sum1[i+1][j+1]+ triangle[i][j])
    print(sum1)
    return sum1[0][0]

l = [[2],[3,4],[6,5,7],[4,1,8,3]]
l2= [[-1],[2,3],[1,-1,-3]]
print(minimumTotal(l2))
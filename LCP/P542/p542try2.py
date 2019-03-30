def updateMatrix( matrix):

    n = len(matrix)
    m = len(matrix[0])

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if matrix[i][j] != 0:
                right = matrix[i][j+1] if j+1 < m else float('inf')
                down = matrix[i+1][j] if i+1 < n else float('inf')
                matrix[i][j] = 1 + min(right, down)
    print(matrix)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                top = matrix[i-1][j] if i-1 >= 0 else float('inf')
                left =  matrix[i][j-1] if j-1 >= 0 else float('inf')
                matrix[i][j] = min(matrix[i][j], 1+min(top, left))
    return matrix



mat = [[0,0,0],[0,1,0],[0,0,0]]
    
mat2 = [[0,0,0],[0,1,0],[1,1,1]]
print(updateMatrix(mat2))
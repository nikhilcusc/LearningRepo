def updateMatrix( matrix):
    for i in range(len(matrix)):
        for j in range(len(i)):
            if matrix[i][j]!=0:
                matrix[i][j] = max(matrix[i-1][j],
                matrix[i][j-1],
                matrix[i+1][j],
                matrix[i][j+1] ) + 1
mat = [[0,0,0],[0,1,0],[0,0,0]]
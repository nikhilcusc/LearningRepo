def updateMatrix( mat):

    row = len(mat)
    col = len(mat[0])
    print(row ,"and ", col)
    mat2 = [[9999 for i in range(col+2)] for j in range(row+2)]
    #print(mat2)
    for i in range(1,row+1):
        for j in range(1, col+1):
            mat2[i][j] = mat[i-1][j-1]

    print("\n After padding ",mat2, "\n")
  
    matrix = mat2
    
    for i in range(1,len(matrix)-1):
        
        for j in range(1,len(matrix[i])-1):
            
            
            if matrix[i][j]!=0:
                matrix[i][j] = min(matrix[i-1][j],
                matrix[i][j-1],
                matrix[i+1][j],
                matrix[i][j+1] ) + 1
            mat[i-1][j-1] = matrix[i][j]
    print(mat)
    
    return mat


mat = [[0,0,0],[0,1,0],[0,0,0]]
    
mat2 = [[0,0,0],[0,1,0],[1,1,1]]
print(updateMatrix(mat))
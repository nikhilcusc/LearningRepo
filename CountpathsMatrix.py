import numpy as np

def paths(matrix):
    path=np.zeros(matrix.shape)
    if matrix[0][0]==0:
        path[0][0] =1

    # make entry in the first row and column of the path matrix
    for i in range(1,len(matrix)):
        if matrix[i][0]==0:
            path[i][0] = path[i-1][0]
    for i in range(1,len(matrix)):
        if matrix[0][i]==0:
            path[0][i]= path[0][i-1]

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix)):
            if matrix[i][j]==0:
                path[i][j] = path[i][j-1] +  path[i-1][j]

    return path[-1][-1]

map1 = [[0,0,0],
        [0,1,0],
        [0,0,0]]
print("The number of paths in the map", map1, " \n is : ",paths(np.asarray(map1)))
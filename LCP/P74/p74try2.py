def matsearch(matrix,target):
    if len(matrix)==0:
        return False
    for i in matrix:
        if len(i)==0:
            return False
    id = len(matrix)
    for i in range(len(matrix)):
        if target>=matrix[i][0]:
            continue  
        else:
            id = i 
    return target in matrix[id-1]

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 34
l = [1,   3,  5,  7]
print(matsearch(matrix,target))
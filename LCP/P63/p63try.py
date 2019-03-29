def uniquePathsWithObstacles(obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid is None:
            return 0
        if obstacleGrid[0] == [0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        print(m,n)
        def paths(m,n):
            #global obstacleGrid
            #print(obstacleGrid)
            if m==1 or n==1:
                return 1
            if obstacleGrid[m][n]==1:
                return 0
            if obstacleGrid[m][n]==0:
                obstacleGrid[m][n] = paths(m-1,n) + paths(m,n-1) 
            return obstacleGrid[m][n]
        
        #print(mat)
        return paths(m-1,n-1)

l  =  [[0]]
l2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
l3=[[0,1]]

print(uniquePathsWithObstacles(l3))
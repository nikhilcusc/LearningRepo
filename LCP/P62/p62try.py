def uniquePaths( m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        mat =[[None for _ in range(n+1)] for _ in range(m+1)]
        
        def paths(m,n):
            if m==1 or n==1:
                return 1
            if mat[m][n]==None:
                mat[m][n] = paths(m-1,n) + paths(m,n-1) 
            return mat[m][n]
        
        #print(mat)
        return paths(m,n)


print(uniquePaths(23,12))
#does not work
#I assumed removing overlapping sets would work, but this assumes that the arrow is shot on the center of the previous balloon, which might not be optimal
def findMinArrowShots( points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    maxarr = len(points)
    counter = 0
    finalarr = points
    finalarr = sorted(finalarr, key=lambda x : x[0])
    print(finalarr)


    i=0
    while i < len(finalarr):
        print(finalarr[i])
        j=i
        print(i,j)
        counter+=1
        while j<len(finalarr)  and  finalarr[j][0] <=finalarr[i][1] :
            j+=1
            maxarr-=1
            #print(maxarr)
        i=j
    return counter


list1 = [[10,16], [2,8], [1,6], [7,12]]
list2 = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]

print(findMinArrowShots(list2))
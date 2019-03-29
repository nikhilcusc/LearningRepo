#back to first approach  
def findMinArrowShots( points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    if len(points)==0:
        return
    
    maxarr = len(points)
    counter = 0
    finalarr = points
    finalarr = sorted(finalarr, key=lambda x : x[1])
    print(finalarr)

    hit = -float("Inf")
    i=0
    for point in finalarr:
        if hit < point[0]:
            counter+=1
            hit = point[1]

    return counter


list1 = [[10,16], [2,8], [1,6], [7,12]]
list2 = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]

print(findMinArrowShots(list2))
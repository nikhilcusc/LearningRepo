# finding overlapping sets : Need more thought development for this approach, 
def findMinArrowShots( points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    
    counter = 0
    finalarr = points
    finalarr = sorted(finalarr, key=lambda x : x[0])
    finalarr2= sorted(finalarr, key=lambda x : x[1])
    print(finalarr)
    i = firstarr = finalarr[0][0]
    lastcoor = finalarr2[-1][1]
    overlappingDict = {}
    while i <= lastcoor:
        overlappingDict[i]=0
        i+=1
    for i in points:
        j = i[0]
        while j <= i[1]:
            overlappingDict[j]+=1
            j+=1
    
    print(overlappingDict)
    vals = list(overlappingDict.values())
    print(len(set(vals)))



list1 = [[10,16], [2,8], [1,6], [7,12]]
list2 = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]

print(findMinArrowShots(list2))
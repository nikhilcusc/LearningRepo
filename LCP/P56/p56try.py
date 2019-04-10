# method 1 : get all the values in dict and create intervals based on that dict
def mergeAdjNum(l):
    r = [[l[0]]]
    for e in l[1:]:
        if r[-1][-1] == e - 1:
            r[-1].append(e)
        else:
            r.append([e])
    return r
def merge( intervals) :
    dict1 = {}
    for i in intervals:
        s = i[0]
        while s <= i[1]:
            try:
                dict1[s]+=1
            except KeyError:
                dict1[s]=1
            s+=1
    print(dict1)
    keys = list(dict1.keys())
    i=0
    int2 =[]
    int2 =  mergeAdjNum(keys)
    int3= []
    for i in int2:
        l=[]
        l.append(i[0])
        l.append(i[-1])
        int3.append(l)
    return int3 


int1 = [[1,3],[2,6],[8,10],[15,18]]
int2 = [[1,4],[4,5]]

print(merge(int2))
def cs(n):
    if n==0:
        return 0
    if n==1:
        return 1
    elif n==2:
        return 2
    
    return cs(n-2)+cs(n-1)

def cs2(n):
    cst =[]
    i=0
    while i<n:
        print(i)
        if i==0:
            cst.append(1)
        elif i==1:
            cst.append(2)
        else:
            
            cst.append(cst[i-1]+cst[i-2])
        
        i+=1
        

    print(cst)
    return cst[n-1]
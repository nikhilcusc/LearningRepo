import math
def reverse(x):
    xr=0
    xl=[]
    while x>=1:

        xl.append(math.floor(x%10))
        x=x/10
    print(xl,len(xl))
    xlen = len(xl)
    xr=0
    x1=0
    while x1 < xlen:
        xr*=10
        xlp=xl.pop(0)
        print(xlp)
        xr=xr+xlp
        
        x1+=1
    
    return xr

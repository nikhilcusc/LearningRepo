# double pointer
l = [1,8,6,2,5,4,8,3,7]
print(max(l),len(l))
maxareas=0
lpointer = 0
rpointer = len(l)-1
while rpointer>lpointer:
    
    if l[rpointer]<l[lpointer]:
        area = (rpointer-lpointer)*l[rpointer]
        rpointer-=1
    else:
        area = (rpointer-lpointer)*l[lpointer]
        lpointer+=1
    
    if area>maxareas:
        maxareas = area
print(maxareas)


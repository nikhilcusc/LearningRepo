l = [1,8,6,2,5,4,8,3,7]
print(max(l),len(l))
areas=[]
for x in range(len(l)):
    fromv = l[x]
    area= []
    for y in range(len(l)):
        hmax = min(fromv,l[y])
        dist = y-x
        area.append(abs(dist*hmax))
    areas.append(area)
print(areas)

print("\n Max areas is : ",(max(areas)))

        
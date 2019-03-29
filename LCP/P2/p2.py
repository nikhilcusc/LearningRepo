list1 = [3,5,2,6,2]
print(list1.pop())
print(list1.pop())
print(list1.pop())
def addTwoNumbers(l1,l2):
    l11 = l1
    l22 = l2
    l3=[]
    l4=[]
    co=0
    iterations = min(len(l11),len(l22))

    if len(l11)>len(l22):
        #print ('l1 is bigger')
        while len(l11)>iterations:
            l4.append(l11.pop())
    elif len(l22)>len(l11):
        #print('l2 is bigger')
        while len(l22)>iterations:
            l4.append(l22.pop())

    while iterations>0 :

        e1=l11.pop()
        e2=l22.pop()

        e3=e1+e2
        if co:
            e3+=1
            co=0
        if e3>=10:
            e3-=10
            co=1

        l3.append(e3)
        iterations-=1

    while len(l4)>0:
        e3 = l4.pop()
        if co:
            e3+=1
            co=0
        if e3>=10:
            e3-=10
            co=1
        l3.append(e3)
    if co:
        l3.append(1)
    #print(l3)
    return l3

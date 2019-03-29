def func(list1):
    lists= []
    print(list1)
    list1.sort()
    num1=0
    while num1 < len(list1)-1:
        l= num1+1
        r=len(list1)-1
        ele = list1[num1]
        print(l)
        ll = list1[l]
        rl = list1[r]
        while l<r:
            templ=[]
            if (ele+list1[l]+list1[r]==0):
                templ.append(list1[l])
                templ.append(ele)
                templ.append(list1[r])
                templ.sort()
                if templ not in lists:
                    lists.append(templ)
                l+=1
                r-=1
            elif (ele+list1[l]+list1[r]<0):
                l+=1
            else:
                r-=1
        num1+=1
    return lists

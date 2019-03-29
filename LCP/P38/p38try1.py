import math

def count1(x,l,i):
    counter=0
    
    while i < len(l):
        if l[i] == x:
            counter+=1
        else:
            return counter
        i+=1 
    return counter
def repstr(list1):
    i=0
    str1=""
    numd = dict([(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(0,'0'),])
    while i< len(list1):
        ival = list1[i]
        countofi = list1[i+1]
        
        str1 = str1 + numd[ival]*countofi
        i+=2
    return str1 
def funct(n):
    list1=[]
    while n >1:
        list1.append(n%10)
        n=math.floor(n/10)
    print(list1)
    count=[]
    i=len(list1)-1
    while i >=0 :
        count.append(list1[i])
        
        c=count1(list1[i],list1,i)
        #print(i,list1)
        count.append(c)
        i-=1
    print(count)
    return repstr(count)

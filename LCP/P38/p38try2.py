import math

def count1(x,l,i):
    counter=0
    print("in count1 function ")
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
    str2=""
    numd = dict([(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(0,'0'),])
    while i< len(list1):
        ival = list1[i]
        countofi = list1[i+1]
        
        str1 = str1 + numd[ival]*countofi + numd[countofi]

        str2 = str2 + numd[ival]*countofi
        i+=2
    print("string in repstr ", str1 , " amd ", str2)
    return str1
def repstr2(list1):
    i=0
    str1=""
    str2=""
    numd = dict([(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(0,'0'),])
    while i< len(list1):
        ival = list1[i]
        #countofi = list1[i+1]
        
        str1 = str1 + numd[ival]

        #str2 = str2 + numd[ival]*countofi
        i+=1
    print("string in repstr ", str1 , " amd ", str2)
    return str1 
def funct(n):
    list1=[]
    
    while n >=1:
        list1.append(n%10)
        n=math.floor(n/10)
    print("Initial list : ",list1)
    count=[]
    list1=list(reversed(list1))
    i=0
    while i <len(list1) :
        #print(i)    
        c=count1(list1[i],list1,i)
        print(i,list1,c)
        count.append(c)
        count.append(list1[i])
        i+=c
    print("Count array : ",count)
    return repstr2(count)

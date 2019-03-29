def ufnc(list1):
  lists = []
  num1=0
  num2=0
  num3=0

  while num1 < len(list1):
    
    num2=num1+1
    while num2<len(list1):
      num3= num2+1
      while num3<len(list1):
        templ=[]
        print(list1[num1],list1[num2],list1[num3])
        if list1[num2]+list1[num3]==(-1*list1[num1]):
          templ.append(list1[num1])
          templ.append(list1[num2])
          templ.append(list1[num3])
          templ.sort()
          if templ not in lists:
            
            lists.append(templ)
        num3+=1
      num2+=1
    num1+=1  
  return lists
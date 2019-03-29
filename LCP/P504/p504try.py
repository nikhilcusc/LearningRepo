def convertToBase7( num):
    """
    :type num: int
    :rtype: str
    """
    neg = False
    if num<0:
        neg = True
        num = abs(num)
    rstr = ""
    while num >=7:
        rstr += str(num%7) 
        #print(rstr)
        num=num//7
    print("rstr now ",rstr)
    if rstr[0]=="0":
        rstr = rstr[1:]
    if neg:
        rstr = "-" + rstr
    return  rstr + str(num)

num = 100
num2 = -7
print(convertToBase7(num2))
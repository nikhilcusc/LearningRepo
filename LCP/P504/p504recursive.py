def convertBaseTo7(num):
    neg = False
    if num<0:
        return '-' + self.convertToBase7(abs(num))
    else:
        if num>=7:
            return str(self.convertToBase7(num//7)) + str(num%7)
        else:
            return str(num)

n = 45
print(convertBaseTo7(n))
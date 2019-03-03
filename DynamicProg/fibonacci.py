import time
import matplotlib.pyplot as plt

memoryTable={}
time_withoutmemoi=[]
time_withmemoi=[]

def fib_withoutmemoi(n):
    if n<=0: return 0
    elif n==1: return 1
    else:
        return fib_withoutmemoi(n-1)+fib_withoutmemoi(n-2)

def fib_withmemoi(n):
    global memoryTable
    if n<=0: return 0
    elif n==1: return 1
    try :
        return (memoryTable[n])
    except KeyError:
        memoryTable[n] = fib_withmemoi(n-1) + fib_withmemoi(n-2)
    return  memoryTable[n]

value =12
#valueend = 100  my computer struggles to compute even 43
valueend = 50
for i in range(valueend):
    startTime = time.time()
    fibval = fib_withoutmemoi(i)
    endTime = time.time()
    print("Time for ", i, " without memoization is ", endTime - startTime)
    time_withoutmemoi.append(endTime - startTime)

for i in range(valueend):
    startTime = time.time()
    fibval = fib_withmemoi(i)
    endTime = time.time()
    print("Time for ", i, " with memoization is ", endTime - startTime)
    time_withmemoi.append(endTime - startTime)


plt.plot(time_withoutmemoi,'g^',time_withmemoi,'r*')

plt.show()
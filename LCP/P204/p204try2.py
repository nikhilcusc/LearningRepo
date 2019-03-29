
def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n<2:
        return 0
    ListPrimes = [True]*n
    ListPrimes[0]=False
    ListPrimes[1]=False

    for i in range(2,n):
        if ListPrimes[i]:
            for j in range(2,(n-1)//i+1):
                ListPrimes[i*j]=False
    return sum(ListPrimes)


print(countPrimes(10))


print(countPrimes(499979))
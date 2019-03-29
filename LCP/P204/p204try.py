#not efficient for really big inputs
def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    def Primes(k):
        if k==4:
            return False
        for i in range(2,k//2):
            
            if k%i==0:
                return False
        return True
    counter=0
    for i in range(2,n):
        
        if Primes(i):
            print(i)
            counter+=1
    return counter
print(countPrimes(10))


print(countPrimes(499979))
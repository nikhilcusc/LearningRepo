import multiprocessing as mp
from DynamicProg import fibonacci



def cube (n): #test function
    return n**3


if __name__ == '__main__':
    pool = mp.Pool(processes=4)
    results = pool.map(fibonacci.fib_withoutmemoi,range(1,40))
    print(results)


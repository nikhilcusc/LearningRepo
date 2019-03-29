#Use bitwise operations to remove the numbers repeated by having them 
def sN(l):
    int ones = 0 
    twos = 0
    for(int i = 0; i < A.length; i++){
        ones = (ones ^ A[i]) & twos;
        twos = (twos ^ A[i]) & ones;
    }
    return ones;

list1 = [2,2,3,2]

print(sN(list1))
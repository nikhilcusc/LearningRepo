from functools import cmp_to_key
def largNum(nums):  
    # The idea is to compare strings instead of integers
    def cmp(a, b):
        print(a,b, int(b + a) - int(a + b))
        return int(b + a) - int(a + b)
        
    nums = list(map(str, nums))
    print(nums)
    nums.sort(key = cmp_to_key(cmp))
    print(nums)
    return ''.join(nums).lstrip('0') or '0'

list1 = [3,30,34,5,9]

print(largNum(list1))
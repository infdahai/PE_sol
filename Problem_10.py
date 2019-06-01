'''

from math import sqrt, floor

prime_list = [2, 3, 5, 7, 11]
n = int(2 * 10E6)
m = 20
def find(k:list,thred : int ) -> int:
    # len(k) > 0
    last = 0
    it = iter(k)
    index = 0
    while True:
        val = next(it,0)
        if val > thred :
            return index,last
        elif val == 0:
            print("Error")
            return -1
        else:
            last = val
            index +=1
            continue


def check(a: int) -> bool:
    (index,val)= find(prime_list,floor(sqrt(a)))
    for i in prime_list[0:index]:
        if a % i == 0:
            return False
    return True

for i in range(13,n):
    if check(i):
        prime_list.append(i)

res = sum(prime_list)
print(res)
'''

import math
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i ==0:
            return False
    else:
        return  True

sum = 2
limit = 2000000
for i in range(3,limit,2):
    if prime(i):
        sum += i
print(sum)

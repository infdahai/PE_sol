'''
  doc : 
    still with problem
'''


import time

begin = time.process_time()

import math


def find_(n: int) -> int:
    a_ = 1
    x = n
    if (x == 1):
        return 1
    for i in range(2, int(math.sqrt(x)) + 1):
        k = 1
        while x % i == 0:
            x = x / i
            k += 1
        a_ *= k
    if ( n == x or n> 1):
        a_ *= 2
    return a_


n = 1
d = 1
limit = 6
k = find_(d)
while (k <= limit):
    n += 1
    d += n
    k = find_(d)
    print(k)
print(d)

end = time.process_time()

res_time = end - begin
print(res_time)

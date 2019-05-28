from math import floor

'''
from bottom to top, reduce numbers that contains some primer numbers. 
'''

n = 10 ** 6
a = [1 for i in range(n + 1)]
# a[2] = 1
# a[3] = 1
p = []
for i in range(2, n):
    if a[i]:
        k = floor(n / i)
        for j in range(1, k + 1):
            a[j * i] = 0

        p.append(i)

print(len(p))
print(p[10**4])

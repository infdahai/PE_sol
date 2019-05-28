"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def prime(k : int):
    i = k-1
    while k% i !=0:
        i -= 1
    if i== 1 :
        return True 
    else:
        return False
res = 2520*2

for i in range(10,20):
    if prime(i):
        res *= i 

print(res)

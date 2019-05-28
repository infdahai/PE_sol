from math import log, sqrt,floor


def prime(k:int):
    i = k-1
    while (k%i !=0):
        i -= 1 
    if( i == 1):
        return True 
    else :
        return False


k = 20 
N = 1 
i = 1 
check = True
limit = sqrt(k)


p =[0] + [t for t in range(2,k+1) if prime(t)]
a = [1 for t in range(len(p))]
while i < len(p) and p[i] <= k:
    if check:
        if p[i] <= limit:
            a[i] = floor(log(k)/log(p[i]))
        else:
            check = False
    
    N = N * p[i]**a[i]
    i += 1 

print(N)

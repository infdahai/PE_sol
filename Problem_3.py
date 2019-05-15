import math
def find_number(x= 600851475143 ):
  max_ = 0
  for i in range(2,int(math.sqrt(x))+1):
    while x % i ==0:
      x = x/i
      if i > max_:
        max_ = i
  print(max_)
find_number()


"""
two optimization consideration : [1.] 2 and fact>3  [2.] fact>3 but fact must less than $sqrt{n}$

n=”the evil big number”
if n mod 2=0
 then
 lastFactor=2
 n=n div 2
 while n mod 2=0
 n=n div 2
else
lastFactor=1
factor=3
maxFactor= n
while n>1 and factor<=maxFactor
if n mod factor=0
 then
 n=n div factor
lastFactor=factor
while n mod factor=0
n=n div factor
maxFactor= n
 factor=factor+2
if n=1
 then
output lastFactor
 else
 output n


"""

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

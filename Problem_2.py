
#  considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


# o,e : odd , even
# seq : 1,0, (1,1,0)*

"""
It's my  understanding mistake. I thought its sum doesn't exceed four million.

sum_val =3 
sum_even = 2
x,y = 3,5
while sum_val < 4000000:
  z = x+y
  sum_val += 2*z
  sum_even += z
  x = y+z 
  y = x+z
sum_even -= z
print(sum_even)
  """
  
  # begin from the third index, [odd,odd,even] is the sequence's rule. so we just consider the third value in [odd,odd,even].
  # because just the z value will influence the final sum value.
  
  sum_even = 2
x,y = 3,5
z = 0
while z < 4000000:
  z = x+y
  sum_even += z
  x = y+z 
  y = x+z
sum_even -= z
print(sum_even)
  
  
  """
  # other's method. I should learn to use filter,lambda 
lst = [1, 2]
count = 1

while True:
    if (lst[count] + lst[count - 1]) < 4*(10**6):
        lst.append(lst[count] + lst[count - 1])
        count += 1
    else:
        break

print(sum(list(filter(lambda x: x % 2 == 0, lst))))
  
  """

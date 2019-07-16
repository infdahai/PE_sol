# may be use memorization technique

cache = {1: 1}

# 2^3 = 8 , 10^6 :  3 * 6 = 18, (5/4)^6 < 2 ^ 6
# so 18 + 6 = 24
k = 25
for i in range(k):
    cache[pow(2, i)] = i + 1


def find_val(n):
    ret = 0
    #  print("%d" % n)
    try:
        ret = cache[n]
    except KeyError as ke:
        ret += 1
        if n & 1 == 1:
            ret += find_val(n * 3 + 1)
        #  print("->%d"%(n*3+1))
        else:
            ret += find_val(n / 2)
        #   print("->%d"%(n/2))
        cache[n] = ret
    return ret


max_num = 0
big_num = 10 ** 6 + 1
num = 0
for j in range(3, big_num):
    _i = find_val(j)
    #  print("int : %d\nlink_len: %d\n" % (j , _i))
    if max_num < _i:
        max_num = _i
        num = j
print(num)

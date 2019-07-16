from functools import reduce

# I am garbage
f = dict()
f[0] = 0
f[1] = len('one')
f[2] = len('two')
f[3] = len('third')
f[4] = len('four')
f[5] = len('five')
f[6] = len('six')
f[7] = len('seven')
f[8] = len('eight')
f[9] = len('nine')
f[10] = len('ten')
f[11] = len('eleven')
f[12] = len('twelve')
f[13] = len('thirteen')
f[14] = len('fourteen')
f[15] = len('fifteen')
f[16] = len('sixteen')
f[17] = len('seventeen')
f[18] = len('eighteen')
f[19] = len('nineteen')
f[20] = len('twenty')
for i in range(3, 10):
    # f[10+i]-f[i]-4+2 + f[i]
    f[i * 10] = f[10 + i] - 2
f[40] = len('forty')
f[1000] = f[1] + 8
for i in range(1, 10):
    f[i * 100] = f[i] + len('hundred')


# print(f[100])
# print(f[15])


def compute(n: int) -> int:
    # 0 < n < 1000
    if n in f.keys():
        return f[n]
    else:
        res = 0
        if n > 99:
            res += f[n - n % 100] + 3
        t = n % 100
        if t > 20:
            res += f[t - t % 10] + f[t % 10]
        else:
            res += f[t]
        f[n] = res
        return res


print(compute(342))

ret = 0
up_bound = 1000

ret = reduce(lambda x, y: x + compute(y), range(up_bound + 1))
print(ret)

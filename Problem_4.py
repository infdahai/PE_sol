def reverse(a: int):
    ret = 0
    while a > 0:
        ret = 10 * ret + a % 10
        a =a// 10
    return ret


def check(a: int):
    return a == reverse(a)


k = 0
a = 999
while a >= 100:
    if a % 11 == 0:
        b = 999
        d = 1
    else:
        b =990
        d = 11
    while b>=a:
        res = a*b
        if res <= k :
            break
        elif check(res):
            k = res
        b -= d
    a -= 1

print(k)

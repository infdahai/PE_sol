input_2 = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''

input_1 = '''08 02 22 97
49 49 99 40
81 49 31 73
52 70 95 23'''


'''
TODO:
    可以考虑根据分块大小，建立前缀积和后缀积，从而快速算出 水平或竖直方向的最大值。消耗是三次n乘法。
'''

input_list = input_2.split('\n')
int_list = []
for l_j in input_list:
    l_j = l_j.split(' ')
    l1 = list(map(int, l_j))
    int_list.append(l1)
max_list =[]
#max_val = 1788696


def leftToRight(a: list) -> int:
    l = len(a)
    val = 0
    for i in range(0, l - 3):
        mul = 1
        for j in range(4):
            if (a[i + j]!=0):
                mul *= a[i + j]
            else:
                mul = 0
                break
        val = max(val,mul)
    return val


max_leftToRight = 0
for list_left in int_list:
    val = leftToRight(list_left)
    max_leftToRight = max(max_leftToRight, val)
max_list.append(max_leftToRight)

def upToDown(a: list) -> int:  # a -> int_list
    l1 = len(a)
    l2 = len(a[0])
    val = 0
    for i in range(l1 - 3):
        mul1 = 1
        for j in range(l2):
            mul2 = 1
            for k in range(4):
                if(a[i + k][j]!=0):
                    mul2 *= a[i + k][j]
                else:
                    mul2 = 0
                    break
            mul1 = max(mul1, mul2)
        val = max(mul1, val)
    return val

max_upToDown = upToDown(int_list)
max_list.append(max_upToDown)

def leftDiagonRight(a:list) -> int : # a -> int_list
    l = len(a)
    val = 0
    for i in range(l-3):
        mul1 = 1
        for j in range(l-3):
            mul2 = 1
            for k in range(4):
                if(a[i+k][j+k]!=0):
                    mul2 *= a[i+k][j+k]
                else:
                    mul2 = 0
                    break
            mul1 = max(mul1, mul2)
        val = max(mul1, val)
    return val

def rightDiagonLeft(a:list) -> int :
    l = len(a)
    val = 0
    for i in range(l - 3):
        mul1 = 1
        for j in range(3,l ):
            mul2 = 1
            for k in range(4):
                if (a[i + k][j - k] != 0):
                    mul2 *= a[i + k][j - k]
                else:
                    mul2 = 0
                    break
            mul1 = max(mul1, mul2)
        val = max(mul1, val)
    return val

max_list.append(leftDiagonRight(int_list))
max_list.append(rightDiagonLeft(int_list))
print(max(max_list))



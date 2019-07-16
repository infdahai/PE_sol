import numpy as np

input_s1 = \
    '''3
    7 4
    2 4 6
    8 5 9 3'''

input_s = \
    '''75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

input_l = []
for elem in input_s.split('\n'):
    temp_ind = list(map(int, elem.lstrip().split(' ')))
    input_l.append(temp_ind)
depth = len(input_l)
mmap = np.array(input_l)
print(mmap)
for i in range(1, depth):
    mmap[i][0] += mmap[i - 1][0]
    mmap[i][i] += mmap[i-1][i-1]
    for j in range(1, i):
        mmap[i][j] += max(mmap[i - 1][j], mmap[i - 1][j - 1])

print(mmap)
max_val = 0
for i in range(depth):
    max_val = max(max_val, mmap[depth - 1][i])

print(max_val)

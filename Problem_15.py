'''
Lattice paths
'''

import numpy as np

map_len = 20

f = np.zeros(shape=(map_len + 1, map_len + 1), dtype=np.float)

f[:, 0] = 1
f[0, :] = 1

for i in range(1, map_len + 1):
    for j in range(1, map_len + 1):
        f[i][j] += f[i - 1][j] + f[i][j - 1]
'''
for i in range(map_len + 1):
    str_row = ''
    for j in range(map_len + 1):
        str_row += ' ' + str(f[i][j])
    print(str_row)
'''
print(f[map_len][map_len])

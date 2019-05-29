

from  math import floor
N = 1000
square = [i**2 for i in range(N//2)]


# a+b =m, a*b = n
for i_in,i_val in enumerate(square):
    for j_in,j_val in enumerate(square):
        if( j_in <=i_in):
            continue
        m = i_in + j_in
        n = i_in * j_in
        if(m>0.5*N and m < floor(2/3*N) ):
            # and m*m>4*n
            if (N*N/2 == N*m - n):
                print(i_in,j_in)
                k = n * (N-m)
                print(k)

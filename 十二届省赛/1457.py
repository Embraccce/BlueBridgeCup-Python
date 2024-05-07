import math
import sys
N = int(input())
for k in range(17,-1,-1):
    l = 2*k-1
    r = max(l,N)+1
    while l+1!=r:
        m = l+r>>1
        if math.comb(m, k) < N:
            l = m
        else:
            r = m
    if math.comb(r,k) == N:
        print(r*(r+1)//2+k+1)
        break
            


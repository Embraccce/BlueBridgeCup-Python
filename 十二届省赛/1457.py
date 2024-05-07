import math
import sys
N = int(input())
for k in range(17,-1,-1):
    l = 2*k
    r = max(l,N)
    while l < r:
        mid = (l + r) // 2
        if math.comb(mid, k) < N:
            l = mid + 1
        else:
            r = mid
    if math.comb(l,k) == N:
        print(l*(l+1)//2+k+1)
        break
            


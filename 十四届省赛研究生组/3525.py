import math
import sys
n = int(input())
arr = [0] + list(map(int,input().split()))
prims = list()
vis = [False for i in range(10**3+1)]
for i in range(2, 10**3+1):
    if not vis[i]:
        prims.append(i)
    j=0
    while i*prims[j]<=10**3:
        vis[i*prims[j]] = True
        if i % prims[j] == 0:
            break
        j+=1


for i in range(1,n+1):
    if arr[i] in prims:
        continue
    else:
        for j in range(i+1,n+1):
            if math.gcd(arr[i], arr[j])!=1:
                print(i, j)
                sys.exit()

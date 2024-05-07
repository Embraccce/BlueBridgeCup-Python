import sys
n = 130000
# Eluer筛
vis = set()
prim = []
for i in range(2, n+1):
    if i not in vis:
        prim.append(i)
    j = 0
    while i * prim[j] <= n:
        vis.add(i * prim[j])
        if i % prim[j] == 0:
            break
        j += 1

while True:
    try:
        print(prim[int(input())-1])
    except:
        break
